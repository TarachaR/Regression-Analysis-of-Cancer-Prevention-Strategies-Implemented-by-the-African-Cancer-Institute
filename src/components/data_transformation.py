import sys
from dataclasses import dataclass

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.linear_model import LinearRegression, Ridge,Lasso

from src.exception import CustomException
from src.logger import logging
import os

from src.utils import save_object

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformer_object(self):
        """
        This function is responsible for data transformation based on the 
        different types of data present in the dataset.
        
        """
        try:
            numerical_columns = ['incidencerate', 'studypercap', 'medianage', 'pctnohs18_24', 'pcths18_24', 'pctbachdeg18_24', 'pcths25_over', 'pctunemployed16_over', 'pctprivatecoveragealone', 'pctasian', 'pctotherrace', 'birthrate']

            num_pipleline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='median')),
                    ('scaler', StandardScaler())
                ]
            )

            logging.info(f"Numerical columns: {numerical_columns} standard scaling completed!")

            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipleline, numerical_columns)
                ]
            )

            return preprocessor
        
        except Exception as e:
            raise CustomException(e, sys)
        
    def initiate_data_transformation(self,train_path,test_path):
            
            try:
                
                # read the train and test data
                train_df = pd.read_csv(train_path)
                test_df = pd.read_csv(test_path)

                logging.info("Read the train and test data as dataframe successfully!")
       
                

                logging.info("Obtaining the preprocessing object")
                # get the preprocessor object
                preprocessing_obj = self.get_data_transformer_object()

                target_column_name = "target_deathrate"
                numerical_columns = ['incidencerate', 'studypercap', 'medianage', 'pctnohs18_24', 'pcths18_24', 'pctbachdeg18_24', 'pcths25_over', 'pctunemployed16_over', 'pctprivatecoveragealone', 'pctasian', 'pctotherrace', 'birthrate']

                input_feature_train_df = train_df.drop(columns=[target_column_name], axis = 1)
                target_feature_train_df=train_df[target_column_name]

                input_feature_test_df = test_df.drop(columns=[target_column_name], axis = 1)
                target_feature_test_df=test_df[target_column_name]

                logging.info(
                    f"Applying preprocessing object on training dataframe and testing dataframe."
                    )
                
                # apply the preprocessor object on the train and test data
                input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
                input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

                logging.info("Preprocessing of the data completed successfully!")

                train_arr = np.c_[
                    input_feature_train_arr, np.array(target_feature_train_df)
                ]

                test_arr = np.c_[
                    input_feature_test_arr, np.array(target_feature_test_df)
                ]

                logging.info(f"Saved preprocessing object.")

                # save the preprocessor object
                save_object(
                    file_path=self.data_transformation_config.preprocessor_obj_file_path,
                    obj = preprocessing_obj
                )

                return(
                        train_arr,
                        test_arr,
                        self.data_transformation_config.preprocessor_obj_file_path,
                )
            
            except Exception as e:
                raise CustomException(e,sys)

