import os
import cv2
import dlib
import numpy as np

# Path to the folder containing images from which faces will be extracted
input_folder_path = r'C:\Users\dades\Music\P\pro'
# Path to the folder where extracted faces will be saved
output_folder_path = r'C:\Users\dades\Music\P\faces'

# Initialize dlib's face detector (HOG-based)
face_detector = dlib.get_frontal_face_detector()
k = 0
# Process each file in the input folder
for filename in os.listdir(input_folder_path):
    try:
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(input_folder_path, filename)
            img = cv2.imread(img_path)
            
            # Convert to grayscale for the face detection
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            faces = face_detector(gray_img, 1)  # Second argument indicates upscaling image 1 time, can be adjusted
            j = 0
            # Extract faces and save
            for i, face_rect in enumerate(faces):
                x, y, w, h = face_rect.left(), face_rect.top(), face_rect.width(), face_rect.height()
                face_img = img[y:y+h, x:x+w]
                cv2.imwrite(os.path.join(output_folder_path, f"{filename}_face_{i}.jpg"), face_img)
                j+=1
                print(f"Extracted face {j} from {filename}")
            k+=1
            print(f"Processed image {k} of {len(os.listdir(input_folder_path))}")
    except:
        print(f"Error processing image {filename}")

print("Face extraction complete.")