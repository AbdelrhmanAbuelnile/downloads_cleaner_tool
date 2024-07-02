#! /usr/bin/env python

import os
import shutil

def clean_downloads():
    downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
    images_path = os.path.join(downloads_path, 'images')
    files_path = os.path.join(downloads_path, 'files')
    other_path = os.path.join(downloads_path, 'other')
    msi_path = os.path.join(downloads_path, 'msi')
    compressed_path = os.path.join(downloads_path, 'compressed')
    videos_path = os.path.join(downloads_path, 'videos')

    os.makedirs(images_path, exist_ok=True)
    os.makedirs(files_path, exist_ok=True)
    os.makedirs(other_path, exist_ok=True)
    os.makedirs(msi_path, exist_ok=True)
    os.makedirs(compressed_path, exist_ok=True)
    os.makedirs(videos_path, exist_ok=True)

    files = os.listdir(downloads_path)

    for file in files:
        file_path = os.path.join(downloads_path, file)
        if os.path.isfile(file_path):
            file_extension = file.split('.')[-1].lower()
            if file_extension in ['png', 'jpg', 'jpeg', 'gif', 'svg']:
                shutil.move(file_path, images_path)
            elif file_extension in ["xlsx", "csv", "pdf", "docx", "pptx", "txt"]:
                shutil.move(file_path, files_path)
            elif file_extension in ["exe", "msi", "bat", "cmd"]:
                shutil.move(file_path, msi_path)
            elif file_extension in ["zip", "rar", "tar", "7z"]:
                shutil.move(file_path, compressed_path)
            elif file_extension in ["mp4", "mkv", "avi", "mov"]:
                shutil.move(file_path, videos_path)
            else:
                shutil.move(file_path, other_path) 

if __name__ == "__main__":
    clean_downloads()
