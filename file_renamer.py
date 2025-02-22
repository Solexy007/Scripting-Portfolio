import os
from datetime import datetime

folder = "test_folder"  # Make a folder with some test files
for filename in os.listdir(folder):
    old_path = os.path.join(folder, filename)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    name, ext = os.path.splitext(filename)
    new_name = f"{name}_{timestamp}{ext}"
    new_path = os.path.join(folder, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed {filename} to {new_name}")