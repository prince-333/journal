import os
# Input folder name
directory = 'climate_samples'
num_files = 0  # Starting the counter of number of files

# Dictionaries: Station ID, Date, Temperature, Percipation.

stations = {}
dates = {}

# String placeholders
most_records_station = '' # Used to determine the station with the most records

# Integer placeholders
missing_records = 0

# Number of Stations as well as processing all files in the folder
directory_list = os.listdir(directory) # Searches the directory for .csv files and counts them.
for file_name in directory_list:     # Goes through every file in the folder
    if file_name.endswith('.csv'):
        num_files += 1
        full_file_path = os.path.join(directory, file_name)
        file = open(full_file_path, 'r')

        lines = file.readlines()
        file.close()

        stations[file_name] = []   # Every file's contents in a list
        
        for line in lines[1:]:  # Only way I can think about to remove the header lol
            line = line.strip('\n')
            components = line.split(',')

            station_id = components[0]
            date = components[1]
            temp = float(components[2])
            precip = float(components[3])
            
            if temp != -999:
            # Stations Tuple to add to dictionary, does not need if statement since it runs before this for loop already.
                stations_tuple = (date, temp, precip)
                stations[file_name].append(stations_tuple)

            # Date Tuple to add to dictionary, needs if statement because values needed are in this loop,
            # so cannot do it beforehand, compared to stations.
                date_tuple = (station_id, temp, precip)

                if date not in dates:
                    dates[date] = []
                dates[date].append(date_tuple) # Finish processing 1 file.
            else: 
                missing_records = missing_records + 1 
                # Will not process the -999 temp error line to the dictionaries,
                # It will also be added towards the missing records counter.


# Find station with the most records
max_records = 0            # Track maximum number of records
for station in stations:
    record_count = len(stations[station])  # Count records for this station
    if record_count > max_records:
        max_records = record_count
        most_records_station = station

num_dates = len(dates) * num_files

# Rewrite these later to assignment strandards, just placeholders for data rn.
print(f'Total number of stations: {num_files}\nTotal number of dates: {num_dates} dates ')
print(f'Station with the most records: {most_records_station.replace('.csv', '')} ')
print(f'Records with missing temperatures: {missing_records}')
print(f'Remaining stations: {len(stations)}')

# Need to question if the most records = original dataset or adjusted data set.

