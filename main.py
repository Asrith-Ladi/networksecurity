from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

import sys
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=='__main__':
    try: 
        logging.info("Enter the try block")
        trainingpipelineconfig=TrainingPipelineConfig()
        dataingestionconfig=DataIngestionConfig(trainingpipelineconfig)
        dataingestion=DataIngestion(dataingestionconfig)
        logging.info("initiated data ingestion")
        dataingestionartifact=dataingestion.initiate_data_ingestion()
        logging.info("Data initiation completed")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data Validation")
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("data Validation Completed")
        print(data_validation_artifact)
        
    except Exception as e :
        logging.info("This will not be printed",e)
        raise NetworkSecurityException(e,sys)