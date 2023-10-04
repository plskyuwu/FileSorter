#!/usr/bin/env python

"""Sorts files in path by their extension and puts them into path for sorted directory"""

__author__ = "plskyuwu"
__copyright__ = "Copyright 2023, plskyuwu"
__credits__ = "plskyuwu"
__license__ = "MIT"
__version__ = "2.0"
__maintainer__ = "plskyuwu"
__email__ = "lotrovec@gmail.com"
__status__ = "Production"

import os
import shutil


def main():
    path = input("Enter Path: ")
    sorted_path = input("Enter Sorted Path (will use path\\Sorted by default): ")
    ignore_folders = input("Ignore folders (Y/N, default = Y)? ")

    # If user doesn't input any path, then default to Sorted folder in path
    if sorted_path == "":
        sorted_path = os.path.join(path, "Sorted")

    if ignore_folders.strip().lower() == "n":
        ignore_folders = False
    else:
        ignore_folders = True

    files = os.listdir(path)

    print()

    for file in files:
        process_file(file, path, sorted_path, ignore_folders)


def process_file(file, path, sorted_path, ignore_folders):
    filename, extension = os.path.splitext(file)
    extension = extension[1:]
    script_filename = os.path.basename(__file__)
    
    if extension == "":
        extension = "Other"

    if file == script_filename:
        print(f"{file} is this script file. Skipping...")
        return

    if filename == "desktop" and extension == "ini":
        print(f"{file} is a protected system file. Skipping...")
        return

    # If this file is a folder and ignore_folders is True then skip
    if os.path.isdir(os.path.join(path, file)) and ignore_folders:
        print(f"{file} is a folder. Skipping...")
        return

    move_file(file, extension, path, sorted_path)


def move_file(file, extension, path, sorted_path):
    destination_path = os.path.join(sorted_path, extension)  # Final folder path, example: C:\Downloads\Sorted\Zip

    # If folder for this file extension doesn't exist, then create it
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
        print(f"Created {destination_path}")

    source_file = os.path.join(path, file)  # Path to the unsorted file, example C:\Downloads\ex.zip
    destination_file = os.path.join(destination_path, file)  # Final file path, example: C:\Downloads\Sorted\Zip\ex.zip
    shutil.move(source_file, destination_file)
    print(f"Moved {file} to {destination_file}")


if __name__ == "__main__":
    main()
    
    print()
    input("Press any key to exit...")
