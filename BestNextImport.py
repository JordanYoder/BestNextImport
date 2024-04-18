import os
from prettytable import PrettyTable


# Function to get the first two characters of a filename
def get_first_two_chars(filename):
    return filename[:2]


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
            first_two_chars = get_first_two_chars(filename)
            file_size = os.path.getsize(file_path)
            if first_two_chars in client_data:
                client_data[first_two_chars]['count'] += 1
                client_data[first_two_chars]['size'] += file_size
            else:
                client_data[first_two_chars] = {'count': 1, 'size': file_size}

    # Sort the client data by filesize in descending order
    sorted_data = sorted(client_data.items(), key=lambda x: x[1]['size'], reverse=True)

    # Create a PrettyTable instance
    table = PrettyTable(['CLIENT', 'COUNT', 'FILESIZE'])

    # Add rows to the table
    for client, data in sorted_data:
        table.add_row([client, data['count'], get_file_size(data['size'])])

    return table


# Path to the "FileMaker Upload Folder"
filemaker_folder_path = r'\\Engagefs\File Conversions\Client Files\FileMaker Upload'
filemaker_table = process_folder(filemaker_folder_path, "FileMaker Upload Folder")

# Path to the "Finder Files Folder"
finder_folder_path = r'\\Engagefs\File Conversions\Client Files\FileMaker Upload\Finder Files'
finder_table = process_folder(finder_folder_path, "Finder Files Folder")

# Concatenate tables horizontally
combined_table = PrettyTable()
combined_table.field_names = ["   FILEMAKER UPLOAD FOLDER (priority)   ", "   FINDER FILES FOLDER (secondary)   "]
combined_table.add_row([str(filemaker_table), str(finder_table)])

# Print the combined table
print(combined_table)
input("Press Enter to Close")
