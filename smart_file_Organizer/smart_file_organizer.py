import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files():
    downloads_folder = folder_path.get()
    if not downloads_folder:
        messagebox.showerror("Error", "Please select a folder first!")
        return

    # File type categories
    categories = {
        "Images": [".png", ".jpg", ".jpeg", ".gif"],
        "Documents": [".pdf", ".docx", ".txt"],
        "Videos": [".mp4", ".mkv"],
        "Music": [".mp3", ".wav"],
        "Archives": [".zip", ".rar"]
    }

    try:
        for file in os.listdir(downloads_folder):
            file_path = os.path.join(downloads_folder, file)
            if os.path.isfile(file_path):
                moved = False
                for category, extensions in categories.items():
                    if file.lower().endswith(tuple(extensions)):
                        category_path = os.path.join(downloads_folder, category)
                        os.makedirs(category_path, exist_ok=True)
                        shutil.move(file_path, os.path.join(category_path, file))
                        moved = True
                        break
                if not moved:  # For uncategorized files
                    others_path = os.path.join(downloads_folder, "Others")
                    os.makedirs(others_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(others_path, file))
        
        messagebox.showinfo("Success", "Files organized successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong: {e}")


def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_path.set(folder_selected)


# Tkinter UI
root = tk.Tk()
root.title("Download Organizer")
root.geometry("500x300")
root.config(bg="#2c3e50")

# Folder Path Variable
folder_path = tk.StringVar()

# Title
title_label = tk.Label(root, text="Download Organizer", font=("Helvetica", 18, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=10)

# Entry + Browse
frame = tk.Frame(root, bg="#2c3e50")
frame.pack(pady=10)

entry = tk.Entry(frame, textvariable=folder_path, width=40, font=("Helvetica", 12))
entry.pack(side=tk.LEFT, padx=5)

browse_btn = tk.Button(frame, text="Browse", command=browse_folder, bg="#16a085", fg="white", font=("Helvetica", 10, "bold"))
browse_btn.pack(side=tk.LEFT, padx=5)

# Organize Button
organize_btn = tk.Button(root, text="Organize Files", command=organize_files, bg="#2980b9", fg="white", font=("Helvetica", 12, "bold"))
organize_btn.pack(pady=20)

# Exit Button
exit_btn = tk.Button(root, text="Exit", command=root.quit, bg="#c0392b", fg="white", font=("Helvetica", 10, "bold"))
exit_btn.pack(pady=10)

root.mainloop()
