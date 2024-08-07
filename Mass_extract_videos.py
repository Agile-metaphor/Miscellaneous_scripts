import cv2
import os

def extract_frames_from_video(video_path, output_folder, frame_rate=1):
    """
    Extracts frames from a video file.
    
    :param video_path: Path to the video file.
    :param output_folder: Folder where extracted frames will be saved.
    :param frame_rate: Rate at which frames will be extracted. 1 means every frame, 2 means every second frame, etc.
    """
    # Make sure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    saved_frame_count = 0

    while success:
        # Save frame every 'frame_rate' frames
        if count % frame_rate == 0:
            # Construct a unique filename for each frame
            frame_filename = os.path.join(output_folder, f"frame_{os.path.basename(video_path).split('.')[0]}_{saved_frame_count}.jpg")
            cv2.imwrite(frame_filename, image)     # Save frame as JPEG file
            saved_frame_count += 1
        success, image = vidcap.read()
        count += 1

def extract_frames_from_videos_in_folder(videos_folder, output_folder, frame_rate=1):
    """
    Extracts frames from all video files in a folder.
    
    :param videos_folder: Folder containing video files.
    :param output_folder: Folder where extracted frames will be saved.
    :param frame_rate: Rate at which frames will be extracted from videos.
    """
    for video_file in os.listdir(videos_folder):
        video_path = os.path.join(videos_folder, video_file)
        # Check if the file is a video (add or modify extensions as needed)
        if video_file.endswith(('.mp4', '.avi', '.mov','mkv')):
            print(f"Extracting frames from {video_file}...")
            extract_frames_from_video(video_path, output_folder, frame_rate)

# Example usage
videos_folder = r'D:\G Play Games\Play Games\current\licenses\OBS'
output_folder = r'C:\Users\dades\Music\P\vidframes'
frame_rate = 1  # Adjust the frame rate as needed

extract_frames_from_videos_in_folder(videos_folder, output_folder, frame_rate)
