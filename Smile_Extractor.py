import cv2
import dlib
import os
import sys
import concurrent.futures
import time
from threading import Lock

# Initialize the detector and smile cascade
detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

# Initialize counters and a lock for thread-safe operations
lock = Lock()
smiles_detected = 0
images_processed = 0

def print_progress_bar(percentage):
    """Prints a simple progress bar."""
    bar_length = 50
    filled_length = int(bar_length * percentage)
    bar = filled_length * '█' + '-' * (bar_length - filled_length)
    print(f'\rProgress: |{bar}| {percentage * 100:.2f}%', end="\r")

def expand_rectangle(rect, img_width, img_height, expand_percent=60):
    """Expands the rectangle by a certain percentage while ensuring it stays within the image bounds."""
    x1, y1, x2, y2 = rect.left(), rect.top(), rect.right(), rect.bottom()
    expand_width = int((x2 - x1) * expand_percent / 100)
    expand_height = int((y2 - y1) * expand_percent / 100)
    x1 = max(0, x1 - expand_width // 2)
    y1 = max(0, y1 - expand_height // 2)
    x2 = min(img_width, x2 + expand_width // 2)
    y2 = min(img_height, y2 + expand_height // 2)
    return (x1, y1, x2, y2)

def process_image(image_path, output_folder, scale_percent=100, total_images=1):
    global smiles_detected, images_processed
    img = cv2.imread(image_path)
    if img is None:
        print(f"\nSkipping {image_path}: Error reading the image.")
        return

    # Resize image to speed up detection
    scaled_img = cv2.resize(img, None, fx=scale_percent/100, fy=scale_percent/100, interpolation=cv2.INTER_AREA)
    gray_img = cv2.cvtColor(scaled_img, cv2.COLOR_BGR2GRAY)

    detections = detector(gray_img, 1)
    for i, d in enumerate(detections):
        x1, y1, x2, y2 = expand_rectangle(d.rect, scaled_img.shape[1], scaled_img.shape[0])
        face = scaled_img[y1:y2, x1:x2]
        gray_face = gray_img[y1:y2, x1:x2]

        # Smile detection
        smiles = smile_cascade.detectMultiScale(gray_face, scaleFactor=3, minNeighbors=50)
        
        if len(smiles) > 0:  # If a smile is detected
            # Update the counters in a thread-safe way
            with lock:
                smiles_detected += 1
                if smiles_detected % 200 == 0:
                    print(f"\nCumulative smiles detected: {smiles_detected} after processing {images_processed} images.")

            orig_x1, orig_y1 = int(x1 * 100 / scale_percent), int(y1 * 100 / scale_percent)
            orig_x2, orig_y2 = int(x2 * 100 / scale_percent), int(y2 * 100 / scale_percent)
            original_face = img[orig_y1:orig_y2, orig_x1:orig_x2]
            cv2.imwrite(os.path.join(output_folder, f"smiling_face_{os.path.basename(image_path)}_{i}.jpg"), original_face)

    with lock:
        images_processed += 1
        print_progress_bar(images_processed / total_images)

def extract_smiling_faces_from_images(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    image_paths = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.png', '.jpg', '.jpeg'))]
    total_images = len(image_paths)
    
    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        tasks = [executor.submit(process_image, image_path, output_folder, 200, total_images) for image_path in image_paths]
        concurrent.futures.wait(tasks)  # Wait for all tasks to complete
    print(f"\nDone processing. Time spent: {time.time() - start_time:.2f} seconds. Total smiles detected: {smiles_detected}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <output_folder>")
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        extract_smiling_faces_from_images(input_folder, output_folder)
