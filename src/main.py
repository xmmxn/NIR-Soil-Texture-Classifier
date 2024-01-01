import tkinter as tk
from tkinter import messagebox
import math
from spectrometercontroller import SpectrometerController
from arduinocontroller import ArduinoController
from prediction import PredictionModels
from soilclassifier import SoilClassifier
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.animation as animation


class SoilTextureClassifier:
    def __init__(self, root, arduino_controller):
        self.root = root
        self.controller = arduino_controller
        self.root.geometry("1280x720")
        self.root.title("NIR Soil Tecture Characterization")

        # Load spectrometer functions
        self.con_spec = SpectrometerController()
        self.con_spec.load_functions()
        self.con_spec.identify_spectrometer()
        self.con_spec.connect_spectrometer()
        self.con_spec.get_information()

        # Inizializations for spectral data
        self.x_values = list(range(1, 117))
        self.y_values = [0] * 116
        self.dark_ref = []
        self.light_ref = []
        self.sample = []
        self.abs_unit = [0] * 116

        # Status for dark, light, and sample measure
        self.dark_status = False
        self.light_status = False

        # Placeholders for soil composition percentage
        # self.sand_percent = None
        # self.silt_precent = None
        # self.clay_percent = None
        # self.classified_soil = None
        self.line_graph()

        # Sand Perentage
        self.sand_label = tk.Label(root, text="Sand %",
                                   font=("Helvetica", 12))
        self.sand_label.pack()

        self.sand_percent = tk.Label(root, text="0",
                                     font=("Helvetica", 12))
        self.sand_percent.pack()
        # Silt Percentage
        self.silt_label = tk.Label(root, text="Silt %",
                                   font=("Helvetica", 12))
        self.silt_label.pack()

        self.silt_percent = tk.Label(root, text="0",
                                     font=("Helvetica", 12))
        self.silt_percent.pack()
        # Clay Percentage
        self.clay_label = tk.Label(root, text="Clay %",
                                   font=("Helvetica", 12))
        self.clay_label.pack()

        self.clay_percent = tk.Label(root, text="0",
                                     font=("Helvetica", 12))
        self.clay_percent.pack()
        # Texture Classification
        self.class_label = tk.Label(root, text="Texture Class",
                                    font=("Helvetica", 12))
        self.class_label.pack()

        self.texture_class = tk.Label(root, text=None,
                                      font=("Helvetica", 12))
        self.texture_class.pack()

        # Button for Dark Reference
        self.dark_button = tk.Button(root, text="Dark Reference",
                                     command=self.dark_callib)
        self.dark_button.pack()

        # Button for Ligth Reference
        self.light_button = tk.Button(root, text="Light Reference",
                                      command=self.light_callib)
        self.light_button.pack()

        # Button for measuring the AU of sample
        self.sample_button = tk.Button(root, text="Measure Sample",
                                       command=self.start_sample)
        self.sample_button.pack()

        # Arduino function buttons
        self.light_on = tk.Button(
            root, text="Light On", command=self.controller.turn_off)
        self.light_on.pack()

        self.light_off = tk.Button(
            root, text="Light Off", command=self.controller.turn_on)
        self.light_off.pack()

    # Dark callibration function
    def dark_callib(self):
        dark = self.con_spec.measure_dark()
        self.dark_status = True
        self.dark_ref = dark  # Might remove this
        self.y_values = dark
        print(self.dark_ref)  # Debugging
        return

    # Light callibration function
    def light_callib(self):
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

    # Start calculating absorbance unit of soil sample
    # The value from this function shall be plotted for visualization
    def start_sample(self):
        if self.dark_status == True and self.light_status == True:
            sample = self.con_spec.measure_sample()
            for i in range(116):
                self.abs_unit[i] = round(-math.log10(sample[i] /
                                        self.light_ref[i]), 4)
            self.y_values = self.abs_unit
            print(self.abs_unit) # Debugging
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

            self.silt_percent.config(text=predict.predict_silt())
            self.clay_percent.config(text=predict.predict_clay())
            self.sand_percent.config(text=predict.predict_sand())
            self.texture_class.config(text=classifier.classify_soil())
        else:
            title = "Warning"
            body = "Please perform callibrations first"
            self.warning_msg(title, body)

        return

    def line_graph(self):
        self.fig = Figure(figsize=(6, 4), dpi=100)
        self.subplot = self.fig.add_subplot(111)
        self.subplot.get_xaxis().set_visible(False)
        self.subplot.get_yaxis().set_visible(False)
        canvas = FigureCanvasTkAgg(self.fig, self.root)
        canvas.draw()
        canvas.get_tk_widget().pack()
        canvas.get_tk_widget().place(x=20)
        update_interval = 1000
        self.animation = animation.FuncAnimation(
            self.fig, self.update_plot, interval=update_interval)

    def update_plot(self, i):
        self.subplot.clear()
        self.subplot.plot(self.x_values, self.y_values)
        self.subplot.get_xaxis().set_visible(False)
        self.subplot.get_yaxis().set_visible(False)

    def warning_msg(self, title, message):
        messagebox.showwarning(title=title, message=message)


if __name__ == "__main__":
    try:
        arduino_controller = ArduinoController()
        # spec_controller = SpectrometerController()
        # Create the main window
        root = tk.Tk()

        # Create an instance of the MyGUI class
        my_gui = SoilTextureClassifier(root, arduino_controller)

        # Start the Tkinter event loop
        root.mainloop()
    except RuntimeError as e:
        print(e)
