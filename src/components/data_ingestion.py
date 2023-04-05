import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    # data ingestion config
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data ingestion method or component")
        try:
            # read the data from the source (can be from anywhere e.g MongoDB, local, etc)
            df = pd.read_csv('notebook\\data\\cancer_clean.csv')
            logging.info("Read the the dataset as dataframe")

            # create the output directory if it does not exist
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            # save the raw data to the output path
            df.to_csv(self.ingestion_config.raw_data_path, index = False, header=True)


            logging.info("Train Test Split Initialized")
            # split the data into train and test
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            
            # save the train and test data to the output path
            train_set.to_csv(self.ingestion_config.train_data_path, index = False, header=True)
            
            # save the train and test data to the output path
            test_set.to_csv(self.ingestion_config.test_data_path, index = False, header=True)

            
            logging.info("Infgestion of the data completed successfully")
            # return the train and test data path
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
           
if __name__ == "__main__":
    obj=DataIngestion()
    obj.initiate_data_ingestion()
