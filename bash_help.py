import os
def generate_execution_batch_file(target_root, script_name):
    subfolders = [f.path for f in os.scandir(target_root) if f.is_dir()]
    
    with open('execute_on_subfolders.bat', 'w') as bat_file:
        bat_file.write("@echo off \n")
        bat_file.write("call conda activate dlib \n")
        for subfolder in subfolders:
            bat_file.write(f"python {script_name} \"{subfolder}\" \"{output_folder}\"\n")
            bat_file.write("timeout /nobreak 10\n")  # Waits for 5 seconds before moving to the next command
    
    print("Batch execution script has been generated.")

# Example usage
target_root = r'C:\Users\dades\Music\P\split_screenshots'  # Same as used before
script_name = r'C:\Users\dades\Documents\Projects\Python\Bots\Image_extractor4.py'  # The Python script to be executed on each subfolder
output_folder = r'C:\Users\dades\Music\P\faces'
generate_execution_batch_file(target_root, script_name)
