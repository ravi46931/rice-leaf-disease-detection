from PIL import Image

# Open an image file
img = Image.open(r"data\Rice Leaf Disease Images\Blast\BLAST1_001.jpg")

# Resize the image
new_size = (128, 128)
resized_img = img.resize(new_size)

# Save the resized image
resized_img.save("resized_image.jpg")
width, height = img.size
print(f"Width: {width}, Height: {height}")