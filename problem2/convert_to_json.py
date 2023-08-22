import argparse
import json
import os

def convert_to_json(input_path, output_path):
    with open(input_path, 'r') as txt_file:
        lines = txt_file.readlines()

    base_filename = os.path.splitext(os.path.basename(input_path))[0]

    json_data = {
        "annotations": [],
        "data": {
            "image": f"/data/upload/{base_filename}.jpg"
        }
    }

    annotations = []
    for line in lines:
        parts = line.strip().split()
        if len(parts) == 5:
            index, x, y, width, height = map(float, parts)
            annotation = {
                "result": [
                    {
                        "image_rotation": 0,
                        "value": {
                            "x": x * 100,
                            "y": y * 100,
                            "width": width * 100,
                            "height": height * 100,
                            "rotation": 0,
                            "rectanglelabels": ["object"]
                        }
                    }
                ]
            }
            annotations.append(annotation)

    json_data["annotations"] = annotations

    with open(output_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert object detection results from text to JSON")
    parser.add_argument("input_path", help="Path to the input text file")
    parser.add_argument("output_path", help="Path to the output JSON file (default: current directory)", nargs='?', default=None)

    args = parser.parse_args()

    if args.output_path is None:
        base_filename = os.path.splitext(os.path.basename(args.input_path))[0]
        args.output_path = f"{base_filename}.json"

    convert_to_json(args.input_path, args.output_path)