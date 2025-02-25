import os
# Original directory
directory = 'C:\\Users\\lmaop\\Desktop\\a\\climate_samples'
num_files = 0  # Starting the counter of number of files

# Dictionaries: Station ID, Date, Temperature, Percipation.

stations = {}
dates = {}

# Number of Stations as well as processing all files in the folder
directory_list = os.listdir(directory) # Searches the directory for .csv files and counts them.
for file_name in directory_list:
    if file_name.endswith('.csv'):
        num_files += 1
        full_file_path = os.path.join(directory, file_name)
        file = open(full_file_path, 'r')

        lines = file.readlines()

        stations[file_name] = []
        for line in lines[1:]:  # Only way I can think about to remove the header lol, and the number of stations is kinda inaccurate
            line = line.strip('\n')

            components = line.split(',')
            station_id = components[0]
            date = components[1]
            temp = float(components[2])
            precip = float(components[3])
            
            # Updating station Dictionary
            station_tuple = (station_id, date, temp, precip)
            stations[file_name].append(station_tuple)

            #Updating dates dictionary
            date_tuple = (date, temp, precip)
            date_list = dates.get(date, [])
            date_list.append(date_tuple)
            dates[date] = date_list
      

        file.close()

# Find station with the most records
most_records_station = ''  # Store station with most records
max_records = 0            # Track maximum number of records
for station in stations:
    record_count = len(stations[station])  # Count records for this station
    if record_count > max_records:
        max_records = record_count
        most_records_station = station

print(f'Finished processing {num_files} stations.')
print(f'Number of stations:', len(stations))
print(f'Number of unique dates:', len(dates))

print(f'{stations}')