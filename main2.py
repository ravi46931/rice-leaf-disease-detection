import os
from PIL import Image
from pathlib import Path
path = Path(r"data\raw\Rice Leaf Disease Images\Tungro")
print(list(path.glob('*')))
list_of_images = list(path.glob('*'))
for image_name in list_of_images:
    img = Image.open(image_name)
    width, height = img.size
    print(f"Width: {width}, Height: {height}")
 
    new_size = (300, 300)
    resized_img = img.resize(new_size)
    # Save the resized image
    # resized_img.save(f"tungro/{image_name}")





# list_of_images = os.listdir(r"data\Rice Leaf Disease Images\Tungro")

# for image_name in list_of_images:
#     img = Image.open(f"data\Rice Leaf Disease Images\Tungro\{image_name}")
#     width, height = img.size
#     print(f"Width: {width}, Height: {height}")

#     new_size = (300, 300)
#     resized_img = img.resize(new_size)
#     # Save the resized image
#     resized_img.save(f"tungro/{image_name}")

# # print(os.listdir(r"data\Rice Leaf Disease Images\Bacterialblight"))