import os
import shutil
import zipfile
import csv
import humanize
import argparse
from datetime import datetime

def extract_images(source_path, dataset_path):
    # Define paths
    extracted_path = os.path.join(dataset_path, "extracted")
    csv_path = os.path.join(dataset_path, "reports")
    
    # Check if the destination folders exist, create if not
    for path in [extracted_path, dataset_path, csv_path]:
        os.makedirs(path, exist_ok=True)
    
    # Unzip the file
    with zipfile.ZipFile(source_path, 'r') as zip_ref:
        zip_ref.extractall(extracted_path)
    
    # Copy images from extracted path to dataset path
    copy_images(extracted_path, dataset_path)
    
    # Delete the extracted folder
    shutil.rmtree(extracted_path)

def copy_images(source, destination):
    for image in os.listdir(source):
        image_path = os.path.join(source, image)
        
        if os.path.isdir(image_path):
            copy_images(image_path, destination)
        elif image.lower().endswith(('.jpg')):
            shutil.copy(image_path, destination)

def folder_count(dataset_path):
    items = os.listdir(dataset_path)
    files = [item for item in items if os.path.isfile(os.path.join(dataset_path, item))]
    return len(files)

def remove_prefix(filename):
    last_dash_index = filename.rfind("-")
    if last_dash_index != -1:
        return filename[last_dash_index + 1:]
    return filename

def generate_unique_filename(base_filename, source):
    index = 1
    new_filename = base_filename
    new_filepath = os.path.join(source, new_filename)
    
    while os.path.exists(new_filepath):
        base, extension = os.path.splitext(base_filename)
        new_filename = f"{base}_{index}{extension}"
        new_filepath = os.path.join(source, new_filename)
        index += 1
        
    return new_filename

def rename_images(dataset_path):
    for filename in os.listdir(dataset_path):
        old_filepath = os.path.join(dataset_path, filename)
        new_filename = remove_prefix(filename)

        if new_filename == filename:
            continue
        
        new_filepath = os.path.join(dataset_path, new_filename)
        new_filename = generate_unique_filename(new_filename, dataset_path)
                        
        try:
            os.rename(old_filepath, os.path.join(dataset_path, new_filename))
        except Exception as e:
            print(f"Error renaming '{old_filepath}' to '{new_filename}': {e}")

def extract_image_details(dataset_path, csv_filename):
    csv_filepath = os.path.join(dataset_path, "reports", csv_filename)

    with open(csv_filepath, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        csv_writer.writerow(["Image", "Image Size", "Image Modification Date"])
        
        for filename in os.listdir(dataset_path):
            image_path = os.path.join(dataset_path, filename)
            
            if os.path.isfile(image_path):
                image_size = humanize.naturalsize(os.path.getsize(image_path))
                modification_date = datetime.fromtimestamp(os.path.getmtime(image_path))
                formatted_date = modification_date.strftime('%a %b %d %H:%M:%S %Y')
                
                csv_writer.writerow([filename, image_size, formatted_date])

def main():
    parser = argparse.ArgumentParser(description="Image Processing Script")
    parser.add_argument("source_path", help="Path to the source zip file")
    parser.add_argument("dataset_path", help="Path to the images_dataset folder")
    args = parser.parse_args()

    SOURCE_PATH = args.source_path
    DATASET_PATH = os.path.join(args.dataset_path, "images_dataset")

    extract_images(SOURCE_PATH, DATASET_PATH)
    
    nfiles_before = folder_count(DATASET_PATH)
    rename_images(DATASET_PATH)
    nfiles_after = folder_count(DATASET_PATH)
    
    print(f"Number of files in the folder BEFORE renaming: {nfiles_before}")
    print(f"Number of files in the folder AFTER renaming: {nfiles_after}")
    
    extract_image_details(DATASET_PATH, "report.csv")

if __name__ == "__main__":
    main()