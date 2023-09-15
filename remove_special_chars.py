import os
import sys

def process_files(folder):
    
    output_folder = os.path.join(os.path.dirname(folder), "txt_files_output")
    if(not os.path.isdir(output_folder)):
        os.mkdir(os.path.join(os.path.abspath(folder),output_folder))

    for file_name in os.listdir(folder):
        input_file_path = os.path.join(folder, file_name)

        output_file_path = os.path.join(output_folder, file_name)

            
        with open(input_file_path, 'r') as file:
            content = file.read()
            cleaned_content = content.replace(',', '').replace('[', '').replace(']', '').strip()
            
        if not os.path.exists(output_file_path):
            with open(output_file_path, 'w') as file:
                file.write(cleaned_content)

try:
    if len(sys.argv) != 2:
        raise ValueError("Exactly one command-line argument is required.")

    folder = sys.argv[1]
    
    if not os.path.exists(folder) or not os.path.isdir(folder):
        raise ValueError("The provided path is not a valid directory.")
    
    process_files(folder)
    print("Files cleaned, special chars removed, and written to new directory:", os.path.join(folder, "txt_files_output"))

except ValueError as ve:
    print(f"Error: {ve}")

