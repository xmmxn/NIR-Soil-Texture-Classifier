# Import necessary libraries
import numpy as np
import joblib


class PredictionModels:
    def __init__(self, sample):
        self.sample = sample
        self.silt_content = None
        self.clay_content = None
        self.silt_model_path = 'C:\\Users\\pacom\\Desktop\\NIR_Soil_Texture_Classifier\\model\\saved_model\\silt_model.joblib'
        self.clay_model_path = 'C:\\Users\\pacom\\Desktop\\NIR_Soil_Texture_Classifier\\model\\saved_model\\clay_model.joblib'

    def predict_sand(self):
        sand = 100 - self.silt_content - self.clay_content
        rounded_sand = round(sand, 2)
        return rounded_sand

    def predict_silt(self):
        load_model = joblib.load(self.silt_model_path)
        reshaped_sample = np.array(self.sample).reshape(1, -1)
        prediction = load_model.predict(reshaped_sample)
        result = round(float(prediction[0][0]), 2)
        self.silt_content = result
        return result

    def predict_clay(self):
        load_model = joblib.load(self.clay_model_path)
        reshaped_sample = np.array(self.sample).reshape(1, -1)
        prediction = load_model.predict(reshaped_sample)
        result = round(float(prediction[0][0]), 2)
        self.clay_content = result
        return result
