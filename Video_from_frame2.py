import cv2
import os
import numpy as np

def resize_and_pad(img, output_size=(1080, 1920)):
    """
    Resize and pad the image to fit the output size while maintaining the aspect ratio.
    
    :param img: Input image.
    :param output_size: Desired output size (width, height).
    :return: Resized and padded image.
    """
    h, w = img.shape[:2]
    desired_w, desired_h = output_size

    # Calculate the scaling factor and new dimensions
    scale = min(desired_w/w, desired_h/h)
    new_w = int(w * scale)
    new_h = int(h * scale)

    # Resize the image
    resized_img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

    # Create a black image of the desired size
    padded_img = np.zeros((desired_h, desired_w, 3), dtype=np.uint8)

    # Compute center offset
    x_offset = (desired_w - new_w) // 2
    y_offset = (desired_h - new_h) // 2

    # Copy img image into center of result image
    padded_img[y_offset:y_offset+new_h, x_offset:x_offset+new_w] = resized_img

    return padded_img

def create_video(images_folder, output_video_path, fps=10, resolution=(1280, 720)):
    """
    Create a video file from images in a folder.
    
    :param images_folder: Folder containing images.
    :param output_video_path: Output path for the video file.
    :param fps: Frames per second for the output video.
    :param resolution: Resolution of the output video.
    """
    # Get all image files
    images = [os.path.join(images_folder, f) for f in os.listdir(images_folder) if f.endswith(('png', 'jpg', 'jpeg'))]
    if not images:
        print("No images found in the specified folder.")
        return
    
    # Sort images by name
    images.sort()

    # Initialize the VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(output_video_path, fourcc, fps, resolution)

    for idx, image_path in enumerate(images, start=1):
        img = cv2.imread(image_path)
        if img is None:
            print(f"Error loading image {image_path}")
            continue

        img = resize_and_pad(img, resolution)
        video.write(img)
        print(f"Processed {idx}/{len(images)} images", end='\r')

    video.release()
    print("\nVideo processing complete.")

# Example Usage
images_folder = r'D:\Projects\Blender\kish\render'
output_video_path = r'D:\Projects\Blender\kish\video.mp4'
create_video(images_folder, output_video_path, fps=24, resolution=(1440, 2560))
