import pickle
import json
import numpy as np
import pandas as pd
import config

class IrisDataset():
    def __init__(self,SepalLengthCm,SepalWidthCm,PetalLengthCm,PetalWidthCm):
        self.SepalLengthCm = SepalLengthCm
        self.SepalWidthCm = SepalWidthCm
        self.PetalLengthCm = PetalLengthCm
        self.PetalWidthCm = PetalWidthCm
        

    def load_model(self):
        with open(config.MODEL_FILE_PATH,'rb') as f:
            
            self.logistic_model = pickle.load(f)


    def get_predict_Species(self):

        self.load_model()
        
        column_names = self.logistic_model.feature_names_in_
        

        test_array = np.zeros(self.logistic_model.n_features_in_) # 4 features
        test_array[0] = self.SepalLengthCm
        test_array[1] = self.SepalWidthCm
        test_array[2] = self.PetalLengthCm
        test_array[3] = self.PetalWidthCm
    
        print("Test Array >>",test_array)

        predicted_Species = self.logistic_model.predict([test_array])

        return predicted_Species
    