#This is simple program that can orginise files based on their type by given path


import os 
import shutil

def create_subfolder_if_needed(folder_path, subfolder_name):
    subfolder_path = os.path.join(folder_path, subfolder_name)
    if not os.path.exists(subfolder_path):
        os.makedirs(subfolder_path)
    return subfolder_path

def clean_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        if os.path.isfile(file_path):
            file_extension = filename.split(".")[-1].lower()
            if file_extension:
                subfolder_name = f"{file_extension.upper()} Files"
                subfolder_path = create_subfolder_if_needed(folder_path, subfolder_name)
                
                new_location = os.path.join(subfolder_path, filename)
                
                if not os.path.exists(new_location):
                    shutil.move(file_path, subfolder_path)
                    print(f"Moved: {filename} -> {subfolder_name}")
                else:
                    print(f"Skipped: {filename} alredy exist in {subfolder_name}")


if __name__ == "__main__":
    folder_path = input("Enter a full path here of directory you want to orgnise: ")
    folder_path = folder_path.strip().strip("'").strip('"')
    
    if os.path.isdir(folder_path):
        clean_folder(folder_path)
        print("Cleaning completed")
    else:
        print("Please give a valid path")
