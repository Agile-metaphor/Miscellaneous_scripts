import cv2
import dlib
import os
import numpy as np

detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")

def resize_image(image, scale_percent=65):
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

def expand_rectangle(rect, img_width, img_height, expand_percent=30):
    """
    Expands the rectangle by a certain percentage while ensuring it stays within the image bounds.
    """
    x1, y1, x2, y2 = rect.left(), rect.top(), rect.right(), rect.bottom()
    width = x2 - x1
    height = y2 - y1
    
    expand_width = int(width * expand_percent / 100)
    expand_height = int(height * expand_percent / 100)
    
    # Ensure expanded rectangle does not go out of image bounds
    x1 = max(0, x1 - expand_width)
    y1 = max(0, y1 - expand_height)
    x2 = min(img_width, x2 + expand_width)
    y2 = min(img_height, y2 + expand_height)
    
    return (x1, y1, x2, y2)

def extract_faces(folder_path, output_folder, batch_size=15):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = [f for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    total_files = len(files)

    def process_batch(batch_files, batch_index):
        for idx, filename in enumerate(batch_files, start=1):
            try:
                print(f"Batch {batch_index}, Processing file {idx}/{len(batch_files)}: {filename}")
                img_path = os.path.join(folder_path, filename)
                img = cv2.imread(img_path)
                img = resize_image(img, scale_percent=65)
                gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                detections = detector(gray_img, 1)
                for i, d in enumerate(detections):
                    # Expand the detected face rectangle to include more of the head
                    x1, y1, x2, y2 = expand_rectangle(d.rect, img.shape[1], img.shape[0])
                    face = img[y1:y2, x1:x2]
                    cv2.imwrite(os.path.join(output_folder, f"face_{filename[:-4]}_{i}.jpg"), face)
            except Exception as e:
                print(f"Failed to process {filename}: {e}")

    for i in range(0, total_files, batch_size):
        batch_files = files[i:i+batch_size]
        process_batch(batch_files, batch_index=i//batch_size + 1)

def main():
    input_folder = r'C:\Users\dades\Music\P\pro'
    output_folder = r'C:\Users\dades\Music\P\faces'
    
    extract_faces(input_folder, output_folder)
    print("Done processing all files.")

if __name__ == "__main__":
    main()
