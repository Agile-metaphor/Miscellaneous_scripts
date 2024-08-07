# import os
# from PIL import Image

# # Set the folder path where the images are stored
# folder_path = r'./General'

# # Define the minimum brightness level
# min_brightness = 128

# # Loop through all the images in the folder
# for file_name in os.listdir(folder_path):
#     # Check if the file is an image
#     if file_name.endswith('.jpg') or file_name.endswith('.png'):
#         # Open the image and get its brightness
#         image_path = os.path.join(folder_path, file_name)
#         image = Image.open(image_path).convert('L')
#         brightness = image.getpixel((0, 0))
        
#         # Check if the brightness is below the minimum threshold
#         if brightness < min_brightness:
#             print(f'{file_name} is a darker image')



import os
import shutil
from PIL import Image

# Define the input and output folders
input_path = r'./General'
output_path = r'./Brighter'

# Set threshold for darkness (adjust as needed)
threshold = 160

# Create output folder if it doesn't exist
if not os.path.exists(output_path):
    os.makedirs(output_path)

# Loop through each image file in the input folder
for filename in os.listdir(input_path):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        # Open image file
        image = Image.open(os.path.join(input_path, filename))

        # Calculate the average brightness of the image
        brightness = sum(image.convert('L').getdata()) / image.size[0] / image.size[1]

        # Check if image is dark
        if brightness > threshold:
            # Copy the dark image to the output folder
            shutil.copy(os.path.join(input_path, filename), os.path.join(output_path, filename))
            print(f'Copied {filename} to {output_path}')

