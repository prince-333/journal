import os

# Directory containing climate data files
directory = 'C:\\Users\\lmaop\\Desktop\\a\\climate_samples'

# Counter for number of files, which equals the number of stations
num_files = 0

# Dictionaries to store climate data
stations = {}  # Key: file name (station ID), Value: list of (date, temp, precip) tuples
dates = {}     # Key: date, Value: list of (station ID, temp, precip) tuples

# Get list of all files in the directory
directory_list = os.listdir(directory)

# Process each file in the directory
for file_name in directory_list:
    if file_name.endswith('.csv'):
        num_files = num_files + 1  # Increment file counter (each file is a station)
        full_file_path = os.path.join(directory, file_name)  # Build full path to file
        file = open(full_file_path, 'r')  # Open file in read mode

        lines = file.readlines()  # Read all lines from the file

        # Use file name (without .csv) as the station identifier
        station_key = file_name[:-4]  # Remove '.csv' extension
        stations[station_key] = []    # Initialize empty list for this station’s data

        # Process each line, skipping the header
        for line in lines[1:]:  # Start from second line to skip header
            line = line.strip('\n')  # Remove trailing newline
            if line:  # Check for non-empty lines
                # Split line into components
                parts = line.split(',')
                station_id = parts[0]  # Station ID from CSV row (for dates dictionary)
                date = parts[1]        # Date from CSV
                temp = float(parts[2]) # Convert temperature to float
                precip = float(parts[3])  # Convert precipitation to float

                # Create tuples per assignment specs
                station_tuple = (date, temp, precip)       # For stations dictionary
                date_tuple = (station_id, temp, precip)    # For dates dictionary

                # Add tuple to stations dictionary using file name as key
                stations[station_key].append(station_tuple)

                # Add tuple to dates dictionary using date as key
                date_list = dates.get(date, [])  # Get existing list or empty list if new
                date_list.append(date_tuple)
                dates[date] = date_list  # Update dictionary with new list

    file.close()  # Close the file after processing

# Find the station with the most records
most_records_station = ''  # To store station with most records
max_records = 0            # To track maximum number of records
for station in stations:
    record_count = len(stations[station])  # Number of records for this station
    if record_count > max_records:
        max_records = record_count         # Update max if current is higher
        most_records_station = station     # Update station name

# Print required output for Task 1
print("Total number of stations:", num_files)
print("Total number of dates:", len(dates))
print("Station with the most records:", most_records_station)

print(f'{stations}')