import os
import shutil

# Define the source and destination directories
source_dir = "slimtoolkit/data"
destination_dir = "results"

# Create the destination directory if it doesn't exist
os.makedirs(destination_dir, exist_ok=True)

# Loop through files in the source directory
for filename in os.listdir(source_dir):
    if filename.endswith(".txt"):
        # Construct the source and destination paths
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)

        # Copy the file to the destination directory
        shutil.copy(source_path, destination_path)
        print(f"Moved: {filename} to {destination_dir}")
        
source_dir = "speaker/data"
for filename in os.listdir(source_dir):
    if filename.endswith(".txt"):
        # Construct the source and destination paths
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)

        # Copy the file to the destination directory
        shutil.copy(source_path, destination_path)
        print(f"Moved: {filename} to {destination_dir}")

source_dir = "confine/results"
for filename in os.listdir(source_dir):
    if filename.endswith(".txt"):
        # Construct the source and destination paths
        source_path = os.path.join(source_dir, filename)
        destination_path = os.path.join(destination_dir, filename)

        # Copy the file to the destination directory
        shutil.copy(source_path, destination_path)
        print(f"Moved: {filename} to {destination_dir}")
