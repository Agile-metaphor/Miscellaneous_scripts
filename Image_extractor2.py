import cv2
import dlib
import os
import numpy as np

# Initialize Dlib's CNN face detector with the model
detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")

def extract_faces(folder_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # List all files in the input folder
    files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    total_files = len(files)
    
    # Process each file
    for idx, filename in enumerate(files, start=1):
        try:
            print(f"Processing file {idx}/{total_files}: {filename}")
            img_path = os.path.join(folder_path, filename)
            img = cv2.imread(img_path)
            
            # Convert to grayscale for the face detection process
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # Detect faces
            detections = detector(gray_img, 1)
            
            # Extract each face found
            for i, d in enumerate(detections):
                x1, y1, x2, y2 = d.rect.left(), d.rect.top(), d.rect.right(), d.rect.bottom()
                face = img[y1:y2, x1:x2]
                cv2.imwrite(os.path.join(output_folder, f"face_{filename[:-4]}_{i}.jpg"), face)
        except Exception as e:
            print(f"Failed to process {filename}: {e}")

def main():
    input_folder = r'C:\Users\dades\Music\P\pro'
    output_folder = r'C:\Users\dades\Music\P\faces'
    
    extract_faces(input_folder, output_folder)
    print("Done processing all files.")

if __name__ == "__main__":
    main()
