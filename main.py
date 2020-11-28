"""Combs through a 1-subdirectory deep hierarchy for non-.json files.  Copies all non-.json files to a separate
destination.

Assumes that all non-.json files have unique names.
"""

import os
import shutil   # Copying and pasting
from tqdm import tqdm

# Parameters
source_path = "E:/Photo Backup/Source/Takeout/Google Photos/"
destination_path = "E:/Photo Backup/Reorganized Files/"

# Check with the user to ensure that they know this will alter files on their computer.
print("WARNING: The purpose of this code is to write files into the folder '" + destination_path + "'.")
print("It might overwrite files that are already there.")
response = input("Do you wish to proceed? (Y/n): ")
if not (response.upper() == "Y"):
    exit()

# Run!
for directory in tqdm([dI for dI in os.listdir(source_path) if os.path.isdir(os.path.join(source_path, dI))]):    # directory is a string
    for file in os.listdir(source_path + directory):
        if not(file[-5:] == ".json"):   # If this name doesn't end with .json:
            shutil.copyfile(source_path + directory + "/" + file, destination_path + file)    # Copy that file to the destination path, keeping its name the same.
