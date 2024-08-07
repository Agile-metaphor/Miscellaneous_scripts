import os
import shutil

def split_into_subfolders(source_folder, target_root, max_images_per_folder=150):
    os.makedirs(target_root, exist_ok=True)
    images = [f for f in os.listdir(source_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
    
    subfolder_number = 0
    for i, image in enumerate(images):
        if i % max_images_per_folder == 0:
            subfolder_number += 1
            subfolder_path = os.path.join(target_root, f"batch_{subfolder_number}")
            os.makedirs(subfolder_path, exist_ok=True)
        
        source_path = os.path.join(source_folder, image)
        destination_path = os.path.join(subfolder_path, image)
        shutil.move(source_path, destination_path)
    
    print(f"Images have been split into {subfolder_number} subfolders.")

# Example usage
source_folder = r'C:\Users\dades\Music\P\Screenshots'
target_root = r'C:\Users\dades\Music\P\split_screenshots'
split_into_subfolders(source_folder, target_root)
