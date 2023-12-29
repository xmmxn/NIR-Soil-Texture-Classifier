import tkinter as tk
import math
from spectrometercontroller import SpectrometerController
from arduinocontroller import ArduinoController


class SoilTextureClassifier:
    def __init__(self, root, arduino_controller):
        self.root = root
        self.controller = arduino_controller
        self.root.geometry("1280x720")
        self.root.title("NIR Soil Tecture Characterization")

        # Add widgets or perform other actions as needed
        self.label = tk.Label(root, text="Hello, Tkinter!",
                              font=("Helvetica", 16))
        self.label.pack(pady=20)

        self.con_spec = SpectrometerController()
        self.con_spec.load_functions()
        self.con_spec.identify_spectrometer()
        self.con_spec.connect_spectrometer()
        self.con_spec.get_information()

        self.dark_ref = []
        self.light_ref = []
        self.sample = []
        self.abs_unit = [0] * 116

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

        self.classify_button = tk.Button(root, text="Classify",
                                         command=self.classify_sample)
        self.classify_button.pack()

        self.light_on = tk.Button(
            root, text="Light On", command=self.controller.turn_off)
        self.light_on.pack()

        self.light_off = tk.Button(
            root, text="Light Off", command=self.controller.turn_on)
        self.light_off.pack()

    # Dark callibration function
    def dark_callib(self):
        dark = self.con_spec.measure_dark()
        self.dark_ref = dark
        print(self.dark_ref)
        return

    # Light callibration function
    def light_callib(self):
        light = self.con_spec.measure_light()
        self.light_ref = light
        print(self.light_ref)
        return

    # Start calculating absorbance unit of soil sample
    # The value from this function shall be plotted for visualization
    def start_sample(self):
        sample = self.con_spec.measure_sample()
        for i in range(116):
            self.abs_unit[i] = round(-math.log10(sample[i] /
                                     self.light_ref[i]), 4)
        print(self.abs_unit)
        return

    # Classifying soil sample based from the AU
    def classify_sample(self):
        return


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
