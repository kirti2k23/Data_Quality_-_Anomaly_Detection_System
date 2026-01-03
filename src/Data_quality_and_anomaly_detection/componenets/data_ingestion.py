import os
from src.Data_quality_and_anomaly_detection.logger import logging
from src.Data_quality_and_anomaly_detection.exception import MycustomException
from src.Data_quality_and_anomaly_detection.utils.common import create_artifacts_dir
import subprocess
from datetime import datetime


class DataIngestion():
    """
    This module will download the online retail datatset and save it at raw folder 
    which is under artifacts folder
    """
    def __init__(self):
        self.datapath = create_artifacts_dir(data_path = "raw")
        self.kaggle_dataset = "jihyeseo/online-retail-data-set-from-uci-ml-repo"
        
    
    def initiate_ingestion(self)->str:
        try:
            if os.path.exists(self.datapath) and os.path.getsize(self.datapath)>0:
                logging.info("Dataset already exist!!!!!!!!!!!!")
                return self.datapath
            logging.info(f"Created {self.datapath} and about to run kaggle command")

            # Build kaggle command line
            cmd = [
            "kaggle","datasets","download",
            "-d", self.kaggle_dataset,
            "-p", self.datapath,
            "--unzip"
            ]

                       
            logging.info(f"started dataset downloading with {cmd} from kaggle at {datetime.now()}")

            # run the command 
            subprocess.run(cmd, check = True)
            logging.info("Kaggle dataset downloaded successfully!!")
    
            if not os.path.exists(self.datapath) or os.path.getsize(self.datapath)==0:
                raise MycustomException("Downloaded file empty or missing")

            dataset_name = "online_retail"
            file_name = f"{dataset_name}.xlsx"

            logging.info(f"Dataset downloaded successfully at {self.datapath} and saved as {file_name}")
            return self.datapath
        except Exception as e:
            raise MycustomException(e)

        

# if __name__ == "__main__":
#     obj = DataIngestion()
#     obj.initiate_ingestion()
