

class SoilClassifier:
    def __init__(self, sand, silt, clay):
        self.sand = sand
        self.silt = silt
        self.clay = clay

    def classify_soil(self):
        if (7 <= self.clay <= 20 and self.sand > 52 and (self.silt + 2 * self.clay) >= 30):
            print("Soil Type: Sandy Loam")
        elif 70 <= self.sand <= 91 and (self.silt + 1.5 * self.clay) >= 15 and (self.silt + 2 * self.clay) < 30:
            print("Soil Type: Loamy Sand")
        elif self.sand > 85 and (self.silt + 1.5 * self.clay) < 15:
            print("Soil Type: Sand")
        elif 7 <= self.clay <= 27 and 28 <= self.silt <= 50 and self.sand <= 52:
            print("Soil Type: Loam")
        elif (50 <= self.silt <= 80 and 12 <= self.clay <= 27) or (50 <= self.silt <= 80 and self.clay < 12):
            print("Soil Type: Silt Loam")
        elif self.silt >= 80 and self.clay < 12:
            print("Soil Type: Silt")
        elif 20 <= self.clay <= 35 and self.silt < 28 and self.sand > 45:
            print("Soil Type: Sandy Clay Loam")
        elif 27 <= self.clay <= 40 and 20 < self.sand <= 46:
            print("Soil Type: Clay Loam")
        elif 27 <= self.clay <= 40 and self.sand <= 20:
            print("Soil Type: Silty Clay Loam")
        elif self.clay >= 35 and self.sand >= 45:
            print("Soil Type: Sandy Clay")
        elif self.clay >= 40 and self.silt >= 40:
            print("Soil Type: Silty Clay")
        elif self.clay >= 40 and self.sand <= 45 and self.silt < 40:
            print("Soil Type: Clay")
        else:
            print("Soil Type: Unclassified")


# def main():
#     continue_loop = 'y'

#     while continue_loop.lower() == 'y':
#         # Input percentages of sand, silt, and clay
#         sand = float(input("Enter the percentage of sand: "))
#         silt = float(input("Enter the percentage of silt: "))
#         clay = float(input("Enter the percentage of clay: "))

#         # Create an instance of the SoilClassifier class
#         soil_classifier = SoilClassifier(sand, silt, clay)

#         # Call the classify_soil method
#         soil_classifier.classify_soil()

#         # Ask if the user wants to continue
#         continue_loop = input(
#             "Do you want to classify another set of soil? (y/n): ")


# if __name__ == "__main__":
#     main()
