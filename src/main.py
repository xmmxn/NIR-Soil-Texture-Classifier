from PIL import Image, ImageTk
from spectrometercontroller import SpectrometerController
from canvas_classifier import canvas_classifier
from spectrometercontroller import SpectrometerController
from arduinocontroller import ArduinoController
from prediction import PredictionModels
from soilclassifier import SoilClassifier
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation
from ttkthemes import ThemedTk
from tooltips import CreateToolTip
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import os
import math


class SoilTextureClassifier:
    def __init__(self, root, arduino_controller):
        self.root = root
        self.controller = arduino_controller
        self.root.geometry("850x450")
        self.root.title("NIR Soil Texture Characterization")

        # Set the window to be fixed size
        self.root.resizable(width=False, height=False)

        # Set the icon for the window
        icon_path = os.path.join(
            "C:\\Users\\pacom\\Desktop\\NIR_Soil_Texture_Classifier\\assets\images", "NIR.ico")
        self.root.iconbitmap(icon_path)

        # Load spectrometer functions
        self.con_spec = SpectrometerController()
        self.con_spec.load_functions()
        self.con_spec.identify_spectrometer()
        self.con_spec.connect_spectrometer()
        self.con_spec.get_information()

        self.x_values = [907, 915, 923, 932, 940, 948, 956, 965, 973, 981, 989, 998, 1006, 1014, 1022, 1031, 1039, 1047, 1055, 1064, 1072, 1080, 1088, 1097, 1105, 1113, 1121, 1130, 1138, 1146, 1154, 1163, 1171, 1179, 1188, 1196, 1204, 1212, 1221, 1229, 1237, 1245, 1254, 1262, 1270, 1278, 1287, 1295, 1303, 1312, 1320, 1328, 1336, 1345, 1353, 1361, 1369, 1378,
                         1386, 1394, 1403, 1411, 1419, 1427, 1436, 1444, 1452, 1461, 1469, 1477, 1485, 1494, 1502, 1510, 1519, 1527, 1535, 1543, 1552, 1560, 1568, 1577, 1585, 1593, 1601, 1610, 1618, 1626, 1635, 1643, 1651, 1660, 1668, 1676, 1684, 1693, 1701, 1709, 1718, 1726, 1734, 1743, 1751, 1759, 1767, 1776, 1784, 1792, 1801, 1809, 1817, 1826, 1834, 1842, 1850, 1859]
        self.y_values = [0] * 116
        self.dark_ref = []
        self.light_ref = []
        self.sample = []
        self.abs_unit = [0] * 116

        # # Status for dark, light, and sample measure
        self.dark_status = False
        self.light_status = False

        self.line_graph()

        # Toolbar
        self.toolbar = tk.Frame(root, bg='#EEF5E8')  # Set background color
        self.toolbar.pack(side=tk.TOP, fill=tk.X,)  # Added padding

        # Folder path for images
        image_folder = "C:\\Users\\pacom\\Desktop\\NIR_Soil_Texture_Classifier\\assets\\images"

        # Load images for buttons
        dark_image = Image.open(os.path.join(image_folder, "dark_image.png"))
        light_image = Image.open(os.path.join(image_folder, "light_image.png"))
        sample_image = Image.open(os.path.join(
            image_folder, "sample_image.png"))
        light_on_image = Image.open(os.path.join(
            image_folder, "light_on_image.png"))
        light_off_image = Image.open(os.path.join(
            image_folder, "light_off_image.png"))

        # Resize images if needed
        icon_size = (20, 20)
        dark_image = dark_image.resize(icon_size)
        light_image = light_image.resize(icon_size)
        sample_image = sample_image.resize(icon_size)
        light_on_image = light_on_image.resize(icon_size)
        light_off_image = light_off_image.resize(icon_size)

        dark_icon = ImageTk.PhotoImage(dark_image)
        light_icon = ImageTk.PhotoImage(light_image)
        sample_icon = ImageTk.PhotoImage(sample_image)
        light_on_icon = ImageTk.PhotoImage(light_on_image)
        light_off_icon = ImageTk.PhotoImage(light_off_image)

        # Add image buttons to the toolbar

        self.light_on = tk.Button(
            self.toolbar, image=light_on_icon, bd=0, bg="#EEF5E8", command=self.controller.turn_off)
        self.light_on.image = light_on_icon
        self.light_on.pack(side=tk.LEFT, padx=5, pady=5)

        self.light_off = tk.Button(
            self.toolbar, image=light_off_icon, bd=0, bg="#EEF5E8", command=self.controller.turn_on)
        self.light_off.image = light_off_icon
        self.light_off.pack(side=tk.LEFT, padx=1, pady=5)

        # Add separator between "Light Off" and "Dark" image button with padding
        self.separator = ttk.Separator(self.toolbar, orient=tk.VERTICAL)
        self.separator.pack(side=tk.LEFT, padx=5, pady=(5, 5), fill=tk.Y)

        # Buttons
        self.dark_button = tk.Button(
            self.toolbar, image=dark_icon, bd=0, bg="#EEF5E8", command=self.dark_calib)
        self.dark_button.image = dark_icon
        self.dark_button.pack(side=tk.LEFT, padx=1, pady=5)

        self.light_button = tk.Button(
            self.toolbar, image=light_icon, bd=0, bg="#EEF5E8", command=self.light_calib)
        self.light_button.image = light_icon
        self.light_button.pack(side=tk.LEFT, padx=1, pady=5)

        self.sample_button = tk.Button(
            self.toolbar, image=sample_icon, bd=0, bg="#EEF5E8", command=self.start_sample)
        self.sample_button.image = sample_icon
        self.sample_button.pack(side=tk.LEFT, padx=1, pady=5)

        # Add tooltips for the buttons
        light_on_tooltip_text = "Lights On"
        self.light_on_tooltip = CreateToolTip(
            self.light_on, light_on_tooltip_text)

        light_off_tooltip_text = "Lights Off"
        self.light_off_tooltip = CreateToolTip(
            self.light_off, light_off_tooltip_text)

        dark_ref_tooltip = "Dark Reference"
        self.dark_ref_tooltip = CreateToolTip(
            self.dark_button, dark_ref_tooltip)

        light_ref_tooltip = "Light Reference"
        self.light_ref_tooltip = CreateToolTip(
            self.light_button, light_ref_tooltip)

        sample_ref_tooltip = "Sample Measurement"
        self.sample_ref_tooltip = CreateToolTip(
            self.sample_button, sample_ref_tooltip)

        # Create an instance of CanvasWindow
        self.canvas_window = canvas_classifier(root)

    def dark_calib(self):
        dark = self.con_spec.measure_dark()
        self.dark_status = True
        self.dark_ref = dark  # Might remove this
        self.y_values = dark
        print(self.dark_ref)  # Debugging
        return
        return

    def light_calib(self):
        if self.dark_status == False:
            title = "Warning"
            body = "Please perform dark callibration first"
            self.warning_msg(title, body)
        else:
            light = self.con_spec.measure_light()
            self.light_ref = light
            self.y_values = light
            self.light_status = True
            print(self.light_ref)
        return

    def start_sample(self):
        if self.dark_status == True and self.light_status == True:
            sample = self.con_spec.measure_sample()
            for i in range(116):
                self.abs_unit[i] = round(-math.log10(sample[i] /
                                                     self.light_ref[i]), 4)
            self.y_values = self.abs_unit
            print(self.abs_unit)  # Debugging
            predict = PredictionModels(self.abs_unit)
            silt_percent = predict.predict_silt()
            clay_percent = predict.predict_clay()
            sand_percent = predict.predict_sand()
            # Debugging
            print(sand_percent)
            print(silt_percent)
            print(clay_percent)

            classifier = SoilClassifier(
                sand_percent, silt_percent, clay_percent)
            classify = classifier.classify_soil()
            self.classified_soil = classify
            print(classify)  # Debugging
            self.canvas_window.silt_value.config(text=predict.predict_silt())
            self.canvas_window.clay_value.config(text=predict.predict_clay())
            self.canvas_window.sand_value.config(text=predict.predict_sand())
            self.canvas_window.texture_text.config(
                text=classifier.classify_soil())
        else:
            title = "Warning"
            body = "Please perform callibrations first"
            self.warning_msg(title, body)
        return

    def line_graph(self):
        self.fig = Figure(figsize=(5, 4), dpi=100)

        self.subplot = self.fig.add_subplot(111)
        # self.subplot.set_facecolor('#EEF5E8')
        self.subplot.set_xlabel('Wavelength')
        self.subplot.plot(self.x_values, self.y_values)

        canvas = FigureCanvasTkAgg(self.fig, self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()
        canvas.get_tk_widget().place(x=20, y=40)
        update_interval = 1000
        self.animation = animation.FuncAnimation(
            self.fig, self.update_plot, interval=update_interval)
        # self.fig.tight_layout()

    def update_plot(self, i):
        self.subplot.clear()
        # self.subplot.set_facecolor('#EEF5E8')
        self.subplot.set_xlabel('Wavelength')
        self.subplot.plot(self.x_values, self.y_values)

        # self.fig.tight_layout()

    def warning_msg(self, title, message):
        messagebox.showwarning(title=title, message=message)


if __name__ == "__main__":
    try:
        root = tk.Tk()
        root.configure(bg='white')
        arduino_controller = ArduinoController()
        my_gui = SoilTextureClassifier(root, arduino_controller)
        root.mainloop()
    except RuntimeError as e:
        print(e)
