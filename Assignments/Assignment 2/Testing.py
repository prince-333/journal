import os

# Input folder name
directory = 'climate_samples'
num_files = 0  # Starting the counter of number of files

# Dictionaries: Station ID, Date, Temperature, Precipitation
stations = {}
dates = {}

# Task 2: Counter for missing records
missing_records_count = 0

# Task 1 & 2: Process all files in the folder and clean data
directory_list = os.listdir(directory)
for file_name in directory_list:
    if file_name.endswith('.csv'):
        num_files = num_files + 1
        full_file_path = os.path.join(directory, file_name)
        file = open(full_file_path, 'r')
        lines = file.readlines()
        file.close()
        
        stations[file_name] = []  # Every file's contents in a list
        
        for line in lines[1:]:  # Skip header
            line = line.strip('\n')
            components = line.split(',')
            
            station_id = components[0]
            date = components[1]
            temp = float(components[2])
            precip = float(components[3])
            
            # Task 2: Remove -999 records at this line
            if temp != -999:  # Only add valid records
                # Stations Tuple
                stations_tuple = (date, temp, precip)
                stations[file_name].append(stations_tuple)
                
                # Date Tuple
                date_tuple = (station_id, temp, precip)
                if date not in dates:
                    dates[date] = []
                dates[date].append(date_tuple)
            else:
                missing_records_count = missing_records_count + 1  # Count removed -999 records

# Task 1: Find station with the most records
most_records_station = ''
max_records = 0
for station in stations:
    record_count = len(stations[station])
    if record_count > max_records:
        max_records = record_count
        most_records_station = station

# Task 1 output
num_dates = len(dates)  # Unique dates
print("Processed", num_files, "stations and", num_dates, "dates.")
print("Station with the most records:", most_records_station.replace('.csv', ''))

# Task 2 output
print("\nCleaning data...")
print("Records with missing temperature:", missing_records_count)
print("Remaining stations after cleaning:", len(stations))
print("\nData cleaning completed.")