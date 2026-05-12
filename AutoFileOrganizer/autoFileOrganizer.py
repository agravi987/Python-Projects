import os
import shutil

# 1. Choose the folder you want to organize
folder_path = r"C:\Users\agpas\Downloads"  # Change this to your folder

# 2. File categories (extensions)
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Videos": [".mp4", ".mkv"],
    "Code": [".py", ".js", ".html", ".css"]
}

# 3. Create folders if not exist
for folder in file_types.keys():
    folder_dir = os.path.join(folder_path, folder)
    if not os.path.exists(folder_dir):
        os.mkdir(folder_dir)

# 4. Organize files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    # Skip if it's a folder
    if os.path.isdir(file_path):
        continue

    # Get file extension
    _, ext = os.path.splitext(file)

    # Check which folder it belongs to
    moved = False
    for folder, extensions in file_types.items():
        if ext.lower() in extensions:
            shutil.move(file_path, os.path.join(folder_path, folder, file))
            print(f"Moved: {file} → {folder}")
            moved = True
            break

    # If file doesn't match any category
    if not moved:
        others_folder = os.path.join(folder_path, "Others")
        if not os.path.exists(others_folder):
            os.mkdir(others_folder)
        shutil.move(file_path, os.path.join(others_folder, file))
        print(f"Moved: {file} → Others")

print("🎉 All files organized successfully!")
