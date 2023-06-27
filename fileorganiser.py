import os
import shutil

path = input("Enter the path to organize: ")

try:
    files = os.listdir(path)
except OSError as e:
    print(f"Error: {e}")
    exit()

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]  # Remove leading dot

    if not extension:
        continue  # Skip files with no extension

    if os.path.exists(os.path.join(path, extension)):
        shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
    else:
        os.makedirs(os.path.join(path, extension))
        shutil.move(os.path.join(path, file), os.path.join(path, extension, file))
