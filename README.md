# eT3 Company Technical Challenge Solution

This documentation provides a step-by-step guide on how to run the solution developed for the eT3 Company Internship Technical Challenge. The solution converts object detection results from a text file into a JSON format for further processing.

## Table of Contents
- [Task 1: Image Dataset Extraction and Reporting](#task-1-image-dataset-extraction-and-reporting)
  - [Task Description](#task-description)
  - [Solution Overview](#solution-overview)
  - [Running the Solution](#running-the-solution)

- [Task 2: Detection System Output Conversion to JSON](#task-2-object-detection-system-output-conversion-to-json)
  - [Task Description](#task-description-1)
  - [Solution Overview](#solution-overview-1)
  - [Running the Solution](#running-the-solution-1)

## Task 1: Image Dataset Extraction and Reporting

### Task Description

In this task, the goal was to extract images from folders and sub-folders, copy them into a single folder, and generate a CSV report containing information about each image.

### Solution Overview

1. **Image Extraction:** The solution recursively searches through the given dataset of images, regardless of the depth of sub-folders. It copies all images to a single folder, discarding any prefixes in the image names.

2. **CSV Report Generation:** For each extracted image, the solution gathers the image name (with the prefix discarded), image size, and the date of the last image content modification. This information is then stored in a CSV report.

### Running the Solution

1. **Input:** Provide the dataset of images in the designated folder structure.

2. **Output:** After running the solution, you will find:
   - All images copied to a single folder `images_dataset`.
   - A CSV report containing the following columns: "Image Name", "Image Size", "Last Modification Date".

3. **Steps:**
   - Execute the script designed for this task.
   - Specify the path to the dataset folder.
   - Run the script.
   - Access the generated CSV report and copied images in the respective output locations.

## Task 2: Object Detection System Output Conversion to JSON

### Task Description

In this task, the objective was to convert the output of a detection system from a TXT file format to a JSON file format for further processing.

### Solution Overview

1. **TXT to JSON Conversion:** The solution takes the TXT output file from the detection system and converts each line's data (object, X, Y, width, height) into a structured JSON format.

2. **JSON Format Creation:** The converted data is organized into a JSON structure that matches the required format for the subsequent system's input.

### Running the Solution

1. **Input:** Provide the TXT output file from the detection system.

2. **Output:** The solution generates a JSON file in the specified format for the subsequent system's input.

3. **Steps:**
   - Execute the script designed for this task.
   - Specify the path to the input TXT file.
   - Run the script.
   - Retrieve the generated JSON file, which can be used as input for the next processing system.

---

By following these instructions, you can effectively run the solutions for both tasks in the eT3 Company Internship Technical Challenge. If you encounter any issues or have questions, please feel free to contact.