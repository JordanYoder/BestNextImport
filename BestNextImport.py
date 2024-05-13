import os
from prettytable import PrettyTable

# Function to get file size in megabytes with two decimal places
def get_file_size(file_size):
    return f"{file_size / (1024 * 1024):.2f} MB"

# Function to process a folder and return a PrettyTable instance
def process_folder(folder_path, folder_name):
    # Dictionary to store counts and file sizes
    client_data = {}

    # Loop through files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            client_data[filename] = {'size': file_size}

    # Sort the client data by filesize in descending order
    sorted_data = sorted(client_data.items(), key=lambda x: x[1]['size'], reverse=True)

    # Create a PrettyTable instance
    table = PrettyTable([folder_name, 'FILESIZE'])

    # Add rows to the table
    for filename, data in sorted_data:
        table.add_row([filename, get_file_size(data['size'])])

    return table


# Path to the "FileMaker Upload Folder"
filemaker_folder_path = r'\\Engagefs\File Conversions\Client Files\FileMaker Upload'
filemaker_table = process_folder(filemaker_folder_path, "FileMaker Upload Folder")

# Print the table
print(filemaker_table)
input("Press Enter to Close")
