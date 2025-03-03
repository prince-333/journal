import os
# Input folder name
directory = 'climate_samples'
num_files = 0  # Starting the counter of number of files.

# Dictionaries: Station ID, Date, Temperature, Percipation.

# Orignal Dataset
raw_station_data = {} 

# Cleaned Dataset
stations = {}
dates = {}

# String placeholders
most_records_station = '' # Used to determine the station with the most records
highest_station = ''
lowest_station = ''
# Extreme Weather Placeholders
first_precipitation = (0.0, '', '')
second_precipitation = (0.0, '', '')
third_precipitation = (0.0, '', '')

highest_temp_date = ''
highest_temp_station = ''

lowest_temp_date = ''
lowest_temp_station = ''

# Integer placeholders
missing_records = 0
highest_avg_trend = -10000.0
lowest_avg_trend = 10000.0

highest_temp = -10000.0
lowest_temp = 10000.0

# For task 5
winter_total = 0.0
winter_count = 0
spring_total = 0.0
spring_count = 0
summer_total = 0.0
summer_count = 0
fall_total = 0.0
fall_count = 0


# Number of Stations as well as processing all files in the folder, then cleaning through the data.
# Task 1 and 2.

directory_list = os.listdir(directory) # Searches the directory for .csv files and counts them.
for file_name in directory_list:     # Goes through every file in the folder.
    if file_name.endswith('.csv'): 
        num_files += 1 # Just tracks how many files are in that folder
        full_file_path = os.path.join(directory, file_name)
        file = open(full_file_path, 'r') 

        lines = file.readlines()
        file.close()
        
        raw_station_data[file_name] = [] # The raw file content in a list
        stations[file_name] = []   # Cleaned file content in a list
        
        for line in lines[1:]:  # Only way I can think about to remove the header lol
            line = line.strip('\n')
            components = line.split(',')

            station_id = components[0]
            date = components[1]
            temp = float(components[2])
            precipitation = float(components[3])
            
            # Tuples for the Raw Data dictionary

            raw_tuple = (date,temp,precipitation)
            raw_station_data[file_name].append(raw_tuple)
            if temp != -999:  # Looks for temp key and does not include any sets components with a tempm of -999.

            # Stations Tuple to add to dictionary, does not need if statement since it runs before 
            # this for loop already.
                stations_tuple = (date, temp, precipitation)
                stations[file_name].append(stations_tuple)

            # Date Tuple to add to dictionary, needs if statement because values needed are in this
            # loop, so cannot do it beforehand, compared to stations.
                date_tuple = (station_id, temp, precipitation)

                if date not in dates:
                    dates[date] = []
                dates[date].append(date_tuple) # Finish processing 1 file.
            else: 
                missing_records = missing_records + 1 
                # Will not process the -999 temp error line to the dictionaries.
                # It will also be added towards the missing records counter.


# Find station with the most records.
max_records = 0 # Track maximum number of records.
for station in raw_station_data:
    record_count = len(raw_station_data[station])  # Count records for this station.
    if record_count > max_records:
        max_records = record_count
        most_records_station = station

# Task 3, Average Temperature
avg_temps = {}

for station in stations:
    count = 0
    record_count = len(stations[station]) 
    if record_count > 0:
        for test in stations[station]:
            temp = test[1]
            count = count + temp
        avg_temp = count / record_count
        avg_temps[station] = avg_temp

for station in avg_temps:
    avg = avg_temps[station]
    if avg > highest_avg_trend:
        highest_avg_trend = float(avg)
        highest_station = station
    if avg < lowest_avg_trend:
        lowest_avg_trend = float(avg)
        lowest_station = station

# Task 4, Extreme Weather Analysis

for station in stations:
    for record in stations[station]:
        date = record[0]
        temp = record[1]
        precipitation = record[2]

        if temp > highest_temp:
            highest_temp = temp
            highest_temp_date = date
            highest_temp_station = station
        if temp < lowest_temp:
            lowest_temp = temp
            lowest_temp_date = date
            lowest_temp_station = station

        if precipitation > first_precipitation[0]:
            third_precipitation = second_precipitation
            second_precipitation = first_precipitation
            first_precipitation = (precipitation, date, station)

        elif precipitation > second_precipitation[0]:
            third_precipitation = second_precipitation
            second_precipitation = (precipitation, date, station)
        elif precipitation > third_precipitation[0]:
            third_precipitation = (precipitation, date, station)

for date in dates:
    month = int(date.split('-')[1])
    for record in dates[date]:
        temp = record[1]
        if month == 12 or month == 1 or month == 2:
            winter_total += temp
            winter_count += 1
        elif month == 3 or month == 4 or month == 5:
            spring_total += temp
            spring_count += 1
        elif month == 6 or month == 7 or month == 8:
            summer_total += temp
            summer_count += 1
        elif month == 9 or month == 10 or month == 11:
            fall_total += temp
            fall_count += 1

if winter_count > 0 and spring_count > 0 and summer_count > 0 and fall_count > 0:
    winter_avg = winter_total / winter_count
    spring_avg = spring_total / spring_count
    summer_avg = summer_total / summer_count
    fall_avg = fall_total / fall_count
else:
    winter_avg = 0.0
    spring_avg = 0.0
    summer_avg = 0.0
    fall_avg = 0.0

# Look through tmrw 
# Rewrite these later to assignment strandards, just placeholders for data rn.
print(f'\nProcessing started...\nProcessed {num_files} stations and {len(dates)} dates\n')
print(f'Station with the most records: {most_records_station.replace('.csv', '')}\n')

print(f'Records with missing temperatures: {missing_records}')
print(f'Remaining stations after cleaning: {len(stations)}\n')

print(f'Station with the highest average temperature is: {highest_station.replace('.csv', '')}')
print(f'With the temperature of {highest_avg_trend:.2f}°C\n')
print(f'Station with the lowest average temperature is: {lowest_station.replace('.csv','')}')
print(f'With the temperature of {lowest_avg_trend:.2f}°C\n')

print('Top 3 precipitation records:')
print(f'{first_precipitation[1]} at Station {first_precipitation[2].replace('.csv', '')}: {first_precipitation[0]:.2f} mm')
print(f'{second_precipitation[1]} at Station {second_precipitation[2].replace('.csv', '')}: {second_precipitation[0]:.2f} mm')
print(f'{third_precipitation[1]} at Station {third_precipitation[2].replace('.csv', '')}: {third_precipitation[0]:.2f} mm\n')

print(f'Highest Temprature: {highest_temp:.2f}°C on {highest_temp_date} at Station {highest_temp_station.replace('.csv','')}')
print(f'Lowest Temprature: {lowest_temp:.2f}°C on {lowest_temp_date} at Station {lowest_temp_station.replace('.csv','')}\n')

print(f'Average temperature in Winter: {winter_avg:.2f}°C\nAverage temperature in Spring: {spring_avg:.2f}°C')
print(f'Average temperature in Summer: {summer_avg:.2f}°C\nAverage temperature in Fall: {fall_avg:.2f}°C')