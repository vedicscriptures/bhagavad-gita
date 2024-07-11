import json
from pathlib import Path

# Define the directory path to start searching for JSON files
dir_path = Path(".")

# Find all JSON files in the directory and its subdirectories
json_files = dir_path.rglob("*.json")

# Iterate over each JSON file found
for file_path in json_files:
    try:
        # Read the JSON content from the source file
        with open(file_path, "r", encoding="utf-8") as source_file:
            data = json.load(source_file)  # Load the JSON data into a Python object

        # Write the JSON content to the target file with pretty formatting
        with open(file_path, "w", encoding="utf-8") as target_file:
            json.dump(data, target_file, ensure_ascii=False, indent=4)  # Dump the JSON data back to the file
            target_file.write("\n")  # Add a newline at the end for better readability

    except Exception as e:
        # Print any exception that occurs during file reading/writing
        print(e)
