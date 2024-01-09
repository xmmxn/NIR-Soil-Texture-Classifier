# Import necessary libraries
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import joblib


class PredictionModels:
    def __init__(self, sample):
        self.sample = sample
        self.sand_content = None
        self.clay_content = None
        self.sand_model_path = 'C:\\Users\\pacom\\Desktop\\NIR_Soil_Texture_Classifier\\model\\saved_model\\sand_model.joblib'
        self.clay_model_path = 'C:\\Users\\pacom\\Desktop\\NIR_Soil_Texture_Classifier\\model\\saved_model\\clay_model.joblib'

    def predict_silt(self):
        silt = 100 - (self.sand_content + self.clay_content)
        rounded_silt = round(silt, 2)
        return rounded_silt

    def predict_sand(self):
        load_model = joblib.load(self.sand_model_path)
        reshaped_sample = np.array(self.sample).reshape(1, -1)
        prediction = load_model.predict(reshaped_sample)
        result = round(float(prediction[0][0]), 2)
        self.sand_content = result
        return result

    def predict_clay(self):
        load_model = joblib.load(self.clay_model_path)
        reshaped_sample = np.array(self.sample).reshape(1, -1)
        prediction = load_model.predict(reshaped_sample)
        result = abs(round(float(prediction[0][0]), 2))
        self.clay_content = result
        return result
