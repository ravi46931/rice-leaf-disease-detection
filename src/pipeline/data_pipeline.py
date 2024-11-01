from src.data.data_augment import ImageAugmentor
from src.data.model import MakeDataset
import sys
from src.exception import CustomException

class DataPipeline:
    def __init__(self, input_dir: str, aug_dir: str):
        self.input_dir = input_dir
        self.aug_dir = aug_dir

    def augment(self):
        try:
            image_augmentor = ImageAugmentor(input_dir=self.input_dir, # change to raw
                                            output_dir=self.aug_dir)
            image_augmentor.augment_images()
        except Exception as e:
            raise CustomException(e, sys)
    
    def create_dataset(self):
        try:
            make_dataset = MakeDataset(dir='data/model', 
                                    aug_path=self.aug_dir, 
                                    orig_path=self.input_dir)     #change to raw
            make_dataset.train_dev_test_split() 

        except Exception as e:
            raise CustomException(e, sys)
    
    def initiate_data_pipeline(self):
        self.augment()
        self.create_dataset()


if __name__ == "__main__":
    data_pipeline = DataPipeline(
        input_dir=r'data\raw\Rice Leaf Disease Images',
        aug_dir=r'data\augmented\Rice Leaf Disease Images'
    )
    data_pipeline.initiate_data_pipeline()