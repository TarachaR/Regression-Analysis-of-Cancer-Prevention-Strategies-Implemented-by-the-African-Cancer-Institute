import sys
import pandas as pd
from src.exception import CustomException
from src.utils import load_object
import os

class PredictPipeline:
    def __init__(self):
        pass

    def predict(self,features):
        try:
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','preprocessor.pkl')
            print("Before Loading")
            model=load_object(file_path=model_path)
            preprocessor=load_object(file_path=preprocessor_path)
            print("After Loading")
            data_scaled=preprocessor.transform(features)
            preds=model.predict(data_scaled)
            return preds
        
        except Exception as e:
            raise CustomException(e,sys)



class CustomData:
    def __init__(   self,
        incidencerate: int,
        studypercap: int,
        medianage: int,
        pctnohs18_24: int,
        pcths18_24: int,
        pctbachdeg18_24: int,
        pcths25_over: int,
        pctunemployed16_over: int,
        pctprivatecoveragealone: int,
        pctasian: int,
        pctotherrace: int,
        birthrate: int):

        self.incidencerate = incidencerate
        self.studypercap = studypercap
        self.medianage = medianage
        self.pctnohs18_24 = pctnohs18_24
        self.pcths18_24 = pcths18_24
        self.pctbachdeg18_24 = pctbachdeg18_24
        self.pcths25_over = pcths25_over
        self.pctunemployed16_over = pctunemployed16_over
        self.pctprivatecoveragealone = pctprivatecoveragealone
        self.pctasian = pctasian
        self.pctotherrace = pctotherrace
        self.birthrate = birthrate


    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict = {
                'incidencerate': [self.incidencerate],
                'studypercap': [self.studypercap],
                'medianage': [self.medianage],
                'pctnohs18_24': [self.pctnohs18_24],
                'pcths18_24': [self.pcths18_24],
                'pctbachdeg18_24': [self.pctbachdeg18_24],
                'pcths25_over': [self.pcths25_over],
                'pctunemployed16_over': [self.pctunemployed16_over],
                'pctprivatecoveragealone': [self.pctprivatecoveragealone],
                'pctasian': [self.pctasian],
                'pctotherrace': [self.pctotherrace],
                'birthrate': [self.birthrate]

            }

            return pd.DataFrame(custom_data_input_dict)
        
        except Exception as e:
            raise CustomException(e, sys) 

