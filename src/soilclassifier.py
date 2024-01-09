

class SoilClassifier:
    def __init__(self, sand, silt, clay):
        self.sand = sand
        self.silt = silt
        self.clay = clay

    def classify_soil(self):
        if (7 <= self.clay <= 20 and self.sand > 52 and (self.silt + 2 * self.clay) >= 30):
            return "SANDY LOAM"
        elif 70 <= self.sand <= 91 and (self.silt + 1.5 * self.clay) >= 15 and (self.silt + 2 * self.clay) < 30:
            return "LOAMY SAND"
        elif self.sand > 85 and (self.silt + 1.5 * self.clay) < 15:
            return "SAND"
        elif 7 <= self.clay <= 27 and 28 <= self.silt <= 50 and self.sand <= 52:
            return "LOAM"
        elif (50 <= self.silt <= 80 and 12 <= self.clay <= 27) or (50 <= self.silt <= 80 and self.clay < 12):
            return "SILTY LOAM"
        elif self.silt >= 80 and self.clay < 12:
            return "SILT"
        elif 20 <= self.clay <= 35 and self.silt < 28 and self.sand > 45:
            return "SANDY CLAY LOAM"
        elif 27 <= self.clay <= 40 and 20 < self.sand <= 46:
            return "CLAY LOAM"
        elif 27 <= self.clay <= 40 and self.sand <= 20:
            return "SILTY CLAY LOAM"
        elif self.clay >= 35 and self.sand >= 45:
            return "SANDY CLAY"
        elif self.clay >= 40 and self.silt >= 40:
            return "SILTY CLAY"
        elif self.clay >= 40 and self.sand <= 45 and self.silt < 40:
            return "CLAY"
        else:
            return "UNCLASSIFIED"
