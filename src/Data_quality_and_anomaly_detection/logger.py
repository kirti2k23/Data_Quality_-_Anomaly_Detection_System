import os
from pathlib import Path
import logging
from datetime import datetime

"""
This folder will do logging and save log files in Logs folder
"""
log_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))),"Logs")
log_file = f"log_file{datetime.now().strftime('%Y%m%%d_%H%M%S')}.log"
os.makedirs(log_folder,exist_ok=True)

Log_file_path = os.path.join(log_folder,log_file)

# Configuration of logging

logging.basicConfig(
    filename=Log_file_path,
    level=logging.INFO,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s- %(message)s"
)

# if __name__ =="__main__":
#     logging.info("Checking logging script")