import os
import shutil

def clean_downloads_directory():
    user_name = os.getlogin()
    downloads_path = f"C:/Users/{user_name}/Downloads"
    count = 0

    for file_system_object in os.listdir(downloads_path):
        path = f"{downloads_path}/{file_system_object}"
        
        if os.path.isfile(path):
            os.remove(path)
            count += 1
        elif os.path.isdir(path):
            shutil.rmtree(path)
            count += 1
        else:
            raise ValueError(f"{path} is neither a file nor directory")

    print(f"Removed {count} file system objects from downloads directory")


if __name__ == "__main__":
    clean_downloads_directory()

