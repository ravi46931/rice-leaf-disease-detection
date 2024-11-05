# Second

import os
import sys
from PIL import Image
import numpy as np
from src.exception import CustomException
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
from typing import Optional
from tensorflow.keras.preprocessing.image import ImageDataGenerator, DirectoryIterator
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class ImageAugmentor:
    def __init__(self, 
                 input_dir: str, 
                 output_dir: str,
                 rotation_range: int = 40,
                 width_shift_range: float = 0.2,
                 height_shift_range: float = 0.2,
                 shear_range: float = 0.2,
                 zoom_range: float = 0.2,
                 horizontal_flip: bool = True,
                 fill_mode: str = 'nearest',
                 target_size: tuple[int, int] = (300, 300), 
                 batch_size: int = 1, 
                 class_mode: str = 'categorical',
                 save_to_dir: Optional[str] = None,
                 save_format: str = 'jpg',
                 num_augmented_images: int = 1):

        self.rotation_range = rotation_range
        self.width_shift_range = width_shift_range
        self.height_shift_range = height_shift_range
        self.shear_range = shear_range
        self.zoom_range = zoom_range
        self.horizontal_flip = horizontal_flip
        self.fill_mode = fill_mode

        # augmentation
        self.input_dir = input_dir
        self.target_size = target_size
        self.batch_size = batch_size
        self.class_mode = class_mode
        self.save_to_dir = save_to_dir
        self.save_format = save_format

        self.output_dir = output_dir
        self.num_augmented_images = num_augmented_images

        self.image_generator = self._get_image_generator()

    def _get_image_generator(self) -> DirectoryIterator:
        
        data_augmentation = ImageDataGenerator(
            rotation_range=self.rotation_range,
            width_shift_range=self.width_shift_range,
            height_shift_range=self.height_shift_range,
            shear_range=self.shear_range,
            zoom_range=self.zoom_range,
            horizontal_flip=self.horizontal_flip,
            fill_mode=self.fill_mode
        )

        image_generator = data_augmentation.flow_from_directory(
            self.input_dir,
            target_size=self.target_size,
            batch_size=self.batch_size,
            class_mode=self.class_mode,
            save_to_dir=self.save_to_dir,  
            save_format=self.save_format
        )

        return image_generator

    def get_class_indices(self) -> dict:
        try:
            class_indices = self.image_generator.class_indices
        except Exception as e:
            raise CustomException(e, sys)
        else:
            reverse_class_indices = {v: k for k, v in class_indices.items()}

        return reverse_class_indices

    def create_dir(self) -> None:
        reverse_class_indices = self.get_class_indices()
        try:
            for class_name in reverse_class_indices.values():
                os.makedirs(os.path.join(self.output_dir, class_name), exist_ok=True)
        except Exception as e:
            raise CustomException(e, sys)

    def augment_images(self):
        class_indices = self.get_class_indices()
        self.create_dir()
        for i in range(len(self.image_generator.filenames)):
            batch_images, batch_labels = self.image_generator[i]  

            # Loop through each image in the batch
            for k in range(batch_images.shape[0]):  
                original_image = batch_images[k]  # Get the k-th image in the batch
                class_label = batch_labels[k]  # Get the corresponding class index
                class_name = class_indices[np.argmax(class_label)]  # Get the class name

                for j in range(self.num_augmented_images):
                    augmented_image = next(self.image_generator)[0][k]  # Get the k-th augmented image in the batch
                    pil_image = Image.fromarray(np.uint8(augmented_image))  # Convert to PIL Image

                    save_path = os.path.join(self.output_dir, class_name, f'augmented_{class_name}_{i}_{j}_{k}.jpg')
                    pil_image.save(save_path)  

if __name__=="__main__":
    # os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0" 
    image_augmentor = ImageAugmentor(input_dir=r'data\raw\Rice Leaf Disease Images', # change to raw
                                    output_dir=r'data\augmented\Rice Leaf Disease Images')
    image_augmentor.augment_images()
