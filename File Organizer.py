# DO NOT STEAL THIS CODE UNLESS GIVEN PERMISSION BY THE CREATOR.

import os
import shutil

FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php", ".rb"],
    "Executables": [".exe", ".bat", ".sh", ".apk"],
}

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            file_ext = os.path.splitext(filename)[1].lower()
            category = next((key for key, exts in FILE_CATEGORIES.items() if file_ext in exts), "Others")
            category_path = os.path.join(directory, category)
            os.makedirs(category_path, exist_ok=True)
            shutil.move(filepath, os.path.join(category_path, filename))
            print(f"Moved: {filename} -> {category}/")

if __name__ == "__main__":
    target_directory = input("Enter the directory path to organize: ").strip()
    organize_files(target_directory)
    print("File organization completed.")
