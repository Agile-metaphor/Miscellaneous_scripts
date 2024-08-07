import cv2
import dlib
import os
import numpy as np
import sys
import time

# Initialize the detector
detector = dlib.cnn_face_detection_model_v1("mmod_human_face_detector.dat")

def resize_image(image, scale_percent=75):
    """Resize the image by the specified scale percent."""
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    return cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

def expand_rectangle(rect, img_width, img_height, expand_percent=35):
    """Expands the rectangle by a certain percentage while ensuring it stays within the image bounds."""
    x1, y1, x2, y2 = rect.left(), rect.top(), rect.right(), rect.bottom()
    width = x2 - x1
    height = y2 - y1
    
    expand_width = int(width * expand_percent / 100)
    expand_height = int(height * expand_percent / 100)
    
    x1 = max(0, x1 - expand_width)
    y1 = max(0, y1 - expand_height)
    x2 = min(img_width, x2 + expand_width)
    y2 = min(img_height, y2 + expand_height)
    
    return (x1, y1, x2, y2)

def print_progress(iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', printEnd="\r"):
    """Call in a loop to create terminal progress bar"""
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()

def extract_faces_from_frame(frame, output_folder, video_name, frame_count):
    """Extract faces from a single frame and save them to the output folder."""
    faces_extracted = 0
    frame = resize_image(frame, scale_percent=75)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detections = detector(gray_frame, 1)
    for i, d in enumerate(detections):
        x1, y1, x2, y2 = expand_rectangle(d.rect, frame.shape[1], frame.shape[0], expand_percent=35)
        face = frame[y1:y2, x1:x2]
        cv2.imwrite(os.path.join(output_folder, f"face_{video_name}_{frame_count}_{i}.jpg"), face)
        faces_extracted += 1
    return faces_extracted

def extract_faces_from_videos(folder_path, output_folder):
    """Process all video files in the given folder and save extracted faces to the output folder."""
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = [f for f in os.listdir(folder_path) if f.endswith(('.mp4', '.avi', '.mov', '.mkv'))]
    total_faces_extracted = 0

    for idx, filename in enumerate(files, start=1):
        video_path = os.path.join(folder_path, filename)
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        frame_count = 0
        
        start_time = time.time()
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Optionally, process only every n-th frame
            if frame_count % 30 == 0:  # Adjust as needed
                try:
                    faces_extracted = extract_faces_from_frame(frame, output_folder, filename[:-4], frame_count)
                    total_faces_extracted += faces_extracted
                except Exception as e:
                    print(f"Failed to process frame {frame_count} in {filename}: {e}")
            print_progress(frame_count + 1, total_frames, prefix=f'Processing {filename}:', suffix='Complete', length=50)
            frame_count += 1

        cap.release()
        end_time = time.time()
        print(f"Done processing video {idx}/{len(files)}: {filename}. Time spent: {end_time - start_time:.2f} seconds. Faces extracted: {total_faces_extracted}")
        total_faces_extracted = 0  # Reset for the next video

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_folder> <output_folder>")
    else:
        input_folder = sys.argv[1]
        output_folder = sys.argv[2]
        extract_faces_from_videos(input_folder, output_folder)
        print("Done processing all files.")