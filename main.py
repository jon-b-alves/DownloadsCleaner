import os
import shutil

downloads_path = r"C:\Users\jjohn\Downloads"
count = 0

for file in os.listdir(downloads_path):
    file_path = f"{downloads_path}\{file}"

    if os.path.isfile(file_path):
        os.remove(file_path)
        count += 1
    elif os.path.isdir(file_path):
        shutil.rmtree(file_path)
        count += 1
    else:
        raise ValueError(f"{file_path} is neither a file or directory")

print(f"Removed {count} files/folders from downloads folder")

