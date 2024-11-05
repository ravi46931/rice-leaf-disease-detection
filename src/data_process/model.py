# third

import os
import shutil
import random
from src.exception import CustomException
from pathlib import Path
from src.data.data_preprocess import DataProcess

class MakeDataset:
    def __init__(self, dir: str, aug_path: str, orig_path: str, train_size: float = 0.8):
        self.dir = dir
        self.aug_path = aug_path
        self.orig_path = orig_path
        self.train_size = train_size

    def get_image_list(self, class_name: str) -> list:
        aug_class_path = os.path.join(self.aug_path, class_name)
        orig_class_path = os.path.join(self.orig_path, class_name)
        aug_image_list = os.listdir(aug_class_path)
        orig_image_list = os.listdir(orig_class_path)

        c_list = [*aug_image_list, *orig_image_list]
        random.shuffle(c_list)

        return c_list

    def split(self, c_list: list, st_index: int, end_index: int):
        images = c_list[st_index : end_index]
        return images

    def get_split_nums(self, c_list: list):
        split_nums = {
                'train': [0, int(len(c_list)*self.train_size)],
                'dev': [int(len(c_list)*self.train_size), int(len(c_list)*(self.train_size + 0.1))],
                'test': [int(len(c_list)*(self.train_size + 0.1)), int(len(c_list))]
            }
        
        return split_nums

    def save(self, class_name: str, images: str, save_dir: str):
        for name in images:
            if name.startswith('augmented'):
                path = os.path.join(self.aug_path, class_name, name)
                shutil.copy(path, save_dir)
            else:
                path = os.path.join(self.orig_path, class_name, name)
                if class_name == 'Tungro':
                    data_process = DataProcess()
                    # change the below code (path)
                    data_process.resize_and_save_images(Path(self.orig_path + '\Tungro\\' + name), Path(save_dir), size=(300, 300))
                else:
                    shutil.copy(path, save_dir)
            # shutil.copy(path, 'data/model/train/Bacterialblight')

    def train_dev_test_split(self):
        classes = ['Bacterialblight', 'Blast', 'Brownspot', 'Tungro']
        splits = ['train', 'dev', 'test']

        for s in splits:
            os.makedirs(f'data/model/{s}', exist_ok=True)
        
        for clas in classes:
            c_list = self.get_image_list(clas)
            split_nums = self.get_split_nums(c_list)
            for s in splits:
                images = self.split(c_list, *split_nums[s])
                os.makedirs(f'data/model/{s}/{clas}', exist_ok=True)
                self.save(clas, images, f'data/model/{s}/{clas}')



if __name__=="__main__":
    make_dataset = MakeDataset(dir='data/model', 
                               aug_path=r'data\augmented\Rice Leaf Disease Images', 
                               orig_path=r'data\raw\Rice Leaf Disease Images')     #change to raw
    make_dataset.train_dev_test_split()   
    
