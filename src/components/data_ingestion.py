#it file is used to split the data into train,test,split. 
#it helps to create artifacts

import os 
import sys #custom exception 
from src.exception import CustomException
from src.logger import logging

import pandas as pd

from sklearn.model_selection import train_test_split
from dataclasses import dataclass # create class variable


# from src.components.data_transformation import DataTransformation
# from src.components.data_transformation import DataTransformationConfig

# where should we keep raw data and test data those input are store in this class
@dataclass
class DataIngestionConfig:
    train_data_path : str=os.path.join('artifacts',"train.csv")  #defining class variable , artifacts fo see the output ,all the output stored in artifacts folder
    test_data_path : str=os.path.join('artifacts',"test.csv")
    raw_data_path : str=os.path.join('artifacts',"raw.csv")



class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig() # above DataIngestionConfig class variable data will be saved to this class variable when we call the DataIngestion class

    def initiate_data_ingestion(self): #read the data from the database
        logging.info("Entered the data Ingestion method or component")

        try:
            df = pd.read_csv("notebook\data\stud.csv") # read the data . we can read this by MangoDB or defrent dataset
            logging.info("Read the dataset as dataframe ")

            #here we creating the directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok = True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False , header=True)

            logging.info("Train test split initiated")
            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            # train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info("Ingestion of the data is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
                
                
            )

        except Exception as e:
            raise CustomException(e,sys)

if __name__ == "__main__":
    obj= DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()


    # data_transformation = DataTransformation()
    # data_transformation.initiate_data_transformation(train_data, test_data)