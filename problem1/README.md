# eT3 Company Technical Challenge Solution - Problem 1

Welcome to the documentation for the solution developed as part of the eT3 Company Internship Technical Challenge. This solution addresses Problem 1, which involves organizing and processing a dataset of images stored in a compressed folder. The solution performs tasks such as extracting images, renaming files, and generating a CSV report.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Setting Up the Environment](#setting-up-the-environment)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Example](#example)

## Overview

The solution automates the process of organizing and processing a dataset of images stored in a compressed folder. It extracts the images, renames the files by removing prefixes, and generates a CSV report containing image details such as image size and modification date.

## Requirements

- Python (version 3.8 or higher)
- Input compressed folder containing images (e.g. `dairies.zip`, see [Example](#example))

### Setting Up the Environment

1. Clone this repository to your local machine:
    ```bash
    git clone <repository_url>
    ```
2. Navigate to the solution directory:
    ```bash
    cd et3-technical-challenge/problem1
    ```
3. Create a virtual environment:
    ```bash
    python -m venv eT3
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        eT3\Scripts\activate
        ```
    - On macOS and Linux:
        ```bash
        source eT3/bin/activate
        ```
5. Install the required packages from the `requirements.txt` file:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the solution script from the command line with the following syntax:
    ```bash
    python organize_images.py <path_to_zip_file> <path_to_output_directory>
    ```
    - `<path_to_zip_file>`: The path to your source compressed folder containing the images.
    - `<path_to_output_directory>`: The desired path to the 'images_dataset' folder directory where the images and CSV report will be saved.
    - This script performs tasks such as extracting images, renaming files, and generating a CSV report.

## File Structure

- `organize_images.py`: Python script for organizing images, renaming files, and generating a CSV report.
- `requirements.txt`: List of Python packages required for the solution script to run.
- `extracted/`: Temporary folder for extracting images during the process.
- `images_dataset/`: Destination folder for organized images and reports.
- `images_dataset/report/`: Folder containing generated CSV reports.

## Example

Assuming you have a source zip file named `dairies.zip` containing images, and you want to organize these images and generate reports in the same directory where the script is located:

1. Place the `dairies.zip` file in the same directory as the script (`organize_images.py`).

2. Navigate to the solution directory:
    ```bash
    cd et3-technical-challenge-solution/problem1
    ```

3. Run the solution script from the command line:
    ```bash
    python organize_images.py dairies.zip .
    ```

After running the script, the images will be organized, files will be renamed, and a CSV report will be generated in seperate directory in the same directory of the images_dataset.