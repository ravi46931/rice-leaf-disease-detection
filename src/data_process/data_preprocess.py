# First
import sys, os
from src.exception import CustomException
from PIL import Image
from pathlib import Path
from src.utils.utils import Resize
import shutil
SIZE: tuple = (300, 300)

class DataProcess:
    def __init__(self):
        pass

    def save_to_process(self, source, dest):
        try:
            shutil.copytree(source, dest, dirs_exist_ok=True)
        except Exception as e:
            raise CustomException(e, sys)
    
    def resize_and_save_images(self, source, dest, size):
        try:
            resizer = Resize(source, dest, size)
            os.makedirs(dest, exist_ok=True)
            resizer.resize_images()
        except Exception as e:
            raise CustomException(e, sys)


if __name__=="__main__":
    data_process = DataProcess()
    raw_path = r'data\raw\Rice Leaf Disease Images'
    process_path = r'data\processed\Rice Leaf Disease Images'
    data_process.save_to_process(raw_path + '\Bacterialblight', process_path + '\Bacterialblight')
    data_process.save_to_process(raw_path + '\Blast', process_path + '\Blast')
    data_process.save_to_process(raw_path + '\Brownspot', process_path + '\Brownspot')
    data_process.resize_and_save_images(Path(raw_path + '\Tungro'), Path(process_path + '\Tungro'), SIZE)
