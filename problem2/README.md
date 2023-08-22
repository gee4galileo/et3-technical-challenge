# eT3 Company Technical Challenge Solution - Problem 2

Welcome to the documentation for the solution developed as part of the eT3 Company Internship Technical Challenge. This solution addresses Problem 2, which involves converting object detection results from a text file into a structured JSON format. The JSON output is designed for further processing and analysis.

## Table of Contents

- [Overview](#overview)
- [Requirements](#requirements)
- [Usage](#usage)
- [File Structure](#file-structure)
- [Example](#example)

## Overview

The solution takes an object detection results text file as input and converts it into a structured JSON format. The JSON format includes object coordinates, dimensions, labels, and other relevant information. This JSON output is suitable for further processing by other systems.

## Requirements

- Python (version 3.8 or higher)
- Input object detection results text file in the specified format (see [Example](#example) below)

## Usage

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/gee4galileo/et3-technical-challenge.git
    ```
2. Navigate to the solution directory:
    ```bash
    cd et3-technical-challenge/problem2
    ```
3. Place your object detection results text file (`detection_results.txt`) inside the solution directory.

4. Run the solution script from the command line with the following syntax:
    ```bash
    python convert_to_json.py input.txt [output.json]
    ```
Replace `[input_file.txt]` with the path to your object detection results text file. If you don't specify an output file path, the script will generate an `[output_file.json]` file in the same directory.

## File Structure

- `convert_to_json.py`: Updated Python script with command-line arguments for converting the object detection results into JSON format.
- `image1.json`: The JSON output file generated after running the script.
- `data/upload/image1.txt`: Sample input object detection results text file.
- `data/upload/image1.json`: The JSON sample result we should achieve.

## Example

### Input (image1.txt)

    ```txt
    0 0.634286 0.175238 0.0914286 0.190476
    0 0.632857 0.393333 0.0942857 0.180952
    ```

### Output (image1.json)

    ```json
    {
        "annotations": [
            {
                "result": [
                    {
                        "image_rotation": 0,
                        "value": {
                            "x": 63.4286,
                            "y": 17.5238,
                            "width": 9.14286,
                            "height": 19.0476,
                            "rotation": 0,
                            "rectanglelabels": ["object"]
                        }
                    }
                ]
            },
            {
                "result": [
                    {
                        "image_rotation": 0,
                        "value": {
                            "x": 63.2857,
                            "y": 39.3333,
                            "width": 9.42857,
                            "height": 18.0952,
                            "rotation": 0,
                            "rectanglelabels": ["object"]
                        }
                    }
                ]
            }
        ],
        "data": {
            "image": "/data/upload/detection_results.jpg"
        }
    }
    ```


