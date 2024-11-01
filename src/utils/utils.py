import sys
from pathlib import Path
from PIL import Image
from src.exception import CustomException

class Resize:
    def __init__(self, input_dir: Path, output_dir: Path, size: tuple[int, int]) -> None:
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.size = size

    def resize_images(self) -> None:
        """
        Resize the images to same size        
        """
        list_of_images = list(self.input_dir.glob('*'))
        try:
            for i, image_name in enumerate(list_of_images):
                img = Image.open(f"{image_name}")
                resized_img = img.resize(self.size)
                resized_img.save(f"{self.output_dir}/{image_name.name}")
                if i%100 == 0:
                    print(f"{i} images resized and saved")
        except Exception as e:
            raise CustomException(e, sys) 
        else:
            print(f"Files successfully resized and saved into {self.output_dir}")
