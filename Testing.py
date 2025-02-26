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
        file.close()

        stations[file_name] = []   # Every file's contents in a list

        for line in lines[1:]:  # Only way I can think about to remove the header lol
            line = line.strip('\n')

            components = line.split(',')
            station_id = components[0]
            date = components[1]
            temp = float(components[2])
            precip = float(components[3])

            # Stations Tuple to add to dictionary, does not need if statement since it runs before this for loop already.
            stations_tuple = (date, temp, precip)
            stations[file_name].append(stations_tuple)

            # Date Tuple to add to dictionary, needs if statement because values needed are in this loop, so cannot do it beforehand compared to stations.
            date_tuple = (station_id, temp, precip)
            if date not in dates:
                dates[date] = []
            else:
                dates[date].append(date_tuple) # Finish processing 1 file.

num_dates = len(dates)
print(f'Total number of stations: {num_files}')
print(f'total number of dates: {num_dates} ')
# Gotta print highest record now.