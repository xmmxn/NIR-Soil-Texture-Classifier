import ctypes
import math


class SpectrometerController:
    def __init__(self):
        self.dll = ctypes.WinDLL(
            r"C:\\Users\\pacom\\Documents\\DLL\\SPECcon.dll")

        # Define the function prototypes
        self.SPEC_Identify = ctypes.WINFUNCTYPE(
            ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p)
        self.SPEC_supported_baudrates = ctypes.WINFUNCTYPE(
            None, ctypes.c_char_p)
        self.SPEC_Connect = ctypes.WINFUNCTYPE(
            ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p)
        self.SPEC_Disconnect = ctypes.WINFUNCTYPE(
            ctypes.c_int, ctypes.c_char_p)
        self.SPEC_Measure = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_int, ctypes.c_float,
                                               ctypes.c_int, ctypes.POINTER(
                                                   ctypes.c_double), ctypes.POINTER(ctypes.c_double),
                                               ctypes.c_int)
        self.SPEC_Execute = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_char_p, ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p,
                                               ctypes.c_char_p)
        self.SPEC_Information = ctypes.WINFUNCTYPE(
            ctypes.c_int, ctypes.c_char_p, ctypes.c_char_p)

        self.port = b"COM3"
        self.baud = 115200
        self.firmware = ctypes.create_string_buffer(1024)
        self.filename = "C:\\Users\\pacom\\Documents\\DLL\\example.txt"
        self.information = ctypes.create_string_buffer(1024)
        self.pixel_count = 128
        self.x_dark = (ctypes.c_double * self.pixel_count)()
        self.y_dark = (ctypes.c_double * self.pixel_count)()
        self.x_ref = (ctypes.c_double * self.pixel_count)()
        self.y_ref = (ctypes.c_double * self.pixel_count)()
        self.integration_time = 10
        self.averages = 10
        self.timeout = 100
        self.wave_start = 8
        self.wave_end = 123

    def load_functions(self):
        self.DLL_supported_baudrates = self.SPEC_supported_baudrates(
            ("SPEC_supported_baudrates", self.dll))
        self.DLL_identify_spectrometer = self.SPEC_Identify(
            ("SPEC_Identify", self.dll))
        self.DLL_connect_spectrometer = self.SPEC_Connect(
            ("SPEC_Connect", self.dll))
        self.DLL_information_spectrometer = self.SPEC_Information(
            ("SPEC_Information", self.dll))
        self.DLL_measure_spectrometer = self.SPEC_Measure(
            ("SPEC_Measure", self.dll))
        self.DLL_execute_commands_from_text_file_spectrometer = self.SPEC_Execute(
            ("SPEC_Execute", self.dll))
        self.DLL_disconnect_spectrometer = self.SPEC_Disconnect(
            ("SPEC_Disconnect", self.dll))

    def identify_spectrometer(self):
        ret = self.DLL_identify_spectrometer(
            self.port, self.baud, self.firmware)
        print(self.port.decode())
        print(self.firmware.value.decode())

    def connect_spectrometer(self):
        filename_bytes = self.filename.encode('utf-8')
        ret = self.DLL_connect_spectrometer(
            self.port, self.baud, filename_bytes)

    def get_information(self):
        ret = self.DLL_information_spectrometer(self.port, self.information)
        print(self.information.value.decode())

    def measure_dark(self):
        ret = self.DLL_measure_spectrometer(self.port, 15, 14, self.integration_time, self.averages, self.x_dark, self.y_dark,
                                            self.timeout)
        dark = []
        print("\nDARK")
        for i in range(self.wave_start, self.wave_end + 1):
            # print(self.x_dark[i], "\t", self.y_dark[i])
            # print(self.x_dark[i])
            dark.append(self.y_dark[i])
        return dark

    def measure_light(self):

        ret = self.DLL_measure_spectrometer(self.port, 16, 14, self.integration_time, self.averages, self.x_ref,
                                            self.y_ref, self.timeout)
        light = []
        print("\nREFERENCE")
        for i in range(self.wave_start, self.wave_end + 1):
            # print(self.x_ref[i], "\t", self.y_ref[i])
            # print(self.y_ref[i])
            light.append(self.y_ref[i])
        return light

    def measure_sample(self):

        ret = self.DLL_measure_spectrometer(self.port, 17, 14, self.integration_time, self.averages, self.x_ref,
                                            self.y_ref, self.timeout)
        sample = []
        print("\nSAMPLE")
        for i in range(self.wave_start, self.wave_end + 1):
            # print(self.x_ref[i], "\t", self.y_ref[i])
            # print(self.x_ref[i], "\t", self.y_ref[i])
            sample.append(self.y_ref[i])
        return sample

    def disconnect_spectrometer(self):
        ret = self.DLL_disconnect_spectrometer(self.port)
        ctypes.windll.kernel32.FreeLibrary(self.dll._handle)
