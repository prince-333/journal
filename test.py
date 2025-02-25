# Import the os module to work with file system operations
import os

# Step 1: Define the folder path where CSV files are stored
folder_path = 'C:\\Users\\lmaop\\Desktop\\a\\climate_samples'  # Replace with your actual folder path

# Step 2: Initialize a counter for CSV files
csv_count = 0

# Step 3: Get a list of all files in the folder and count CSV files
file_list = os.listdir(folder_path)  # Returns a list of all files and directories in folder_path
for file_name in file_list:
    if file_name.endswith(".csv"):   # Check if the file ends with .csv
        csv_count = csv_count + 1    # Increment counter if it's a CSV file

# Step 4: Print the total number of CSV files found
print("Total number of CSV files:", csv_count)

# Step 5: Access and display basic info about each CSV file
for file_name in file_list:
    if file_name.endswith(".csv"):
        full_path = os.path.join(folder_path, file_name)  # Create full file path
        print("\nProcessing file:", file_name)
        
        # Step 6: Open and read the CSV file
        file = open(full_path, "r")  # Open the file in read mode
        content = file.read()        # Read all content into a string
        lines = content.split("\n")  # Split content into lines

        # Step 7: Count and display basic statistics
        line_count = 0
        for line in lines:
            if line:                 # Check if line is not empty
                line_count = line_count + 1
        
        print("Number of lines:", line_count)
# Step 10: Final summary
print("\nFinished processing all CSV files in", folder_path)