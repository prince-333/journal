'''

Quick note, [] in the comments indicate the line number, e.g., [16] referes to this line.

'''


import os
# Input folder name below
directory = 'climate_samples' # Processing of the folder starts at [76]
num_files = 0  # Starting the counter of number of files.

# The following are dictionaries organized as such the assignments needs.

# Orignal Dataset
raw_station_data = {}  # (date,temp,precip)

# Cleaned Dataset
stations = {} # (date, temperature, precip).
dates = {} # (station ID, temperature, precip).
avg_temps = {} # Placeholder for the avg temp [145].

# String placeholders
most_records_station = ''   # Used to determine the station with the most records
highest_station = ''        # Highest Average station
lowest_station = ''         # Lowest Average station.
# Extreme Weather Placeholders
first_precip = (0.0, '', '')    # (precip, date, station)
second_precip = (0.0, '', '')
third_precip = (0.0, '', '')
#Highest recorded temp and lowest recorded temp placeholders
highest_temp_date = ''          
highest_temp_station = ''

lowest_temp_date = ''
lowest_temp_station = ''

# Integer placeholders
missing_records = 0          # Starts the count of missing records with temp = -999
highest_avg_trend = -10000.0 # In general any REALLY SMALL number
lowest_avg_trend = 10000.0   # Any REALLY BIG number, same concept applies below [57 - 58]

highest_temp = -10000.0
lowest_temp = 10000.0

# Seasonal calculation placeholders [189-199]
# Float values represents the temp (which is a float in the dataset), while the integer is the
# count of that tuple after adding the specified temp value.

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

directory_list = os.listdir(directory) # Returns a list of all files in the specified folder [24]
for file_name in directory_list:     # Goes through every file in the list [77].
    if file_name.endswith('.csv'):   # Reads only .csv files.
        num_files += 1 # Just tracks how many files are in the list .
        full_file_path = os.path.join(directory, file_name) # Open each file OS independently.
        file = open(full_file_path, 'r') # Opens the file in read moode.
        # Strandard procedure to read lines [83-84] [89-97]
        lines = file.readlines()
        file.close()
        
        raw_station_data[file_name] = [] # The raw file content in a list
        stations[file_name] = []   # Cleaned file content in a list
        
        for line in lines[1:]:  # [1:] removes the header in each file.
            line = line.strip('\n')
            components = line.split(',')

            # Indexing the components to designated variables
            station_id = components[0]
            date = components[1]
            temp = float(components[2])
            precip = float(components[3])
            
            # Tuples for the Raw Data dictionary

            raw_tuple = (date,temp,precip)
            raw_station_data[file_name].append(raw_tuple)
            if temp != -999:  # Goes through the temp key and does not include 
                              # any components with a temp of -999.

            # Stations Tuple to add to dictionary, does not need if statement since it runs before 
            # this for loop already. [87]
                stations_tuple = (date, temp, precip)
                stations[file_name].append(stations_tuple)

            # Date Tuple to add to dictionary, needs if statement because values needed are in this
            # loop, so cannot do it beforehand, compared to stations. [115-119]
                date_tuple = (station_id, temp, precip)
                
                if date not in dates: # Creating a new list to append the data_tuple 
                    dates[date] = [] 
                dates[date].append(date_tuple) # Finish processing 1 file.
            else: 
                missing_records = missing_records + 1 
                # Will not process the -999 temp error line to the dictionaries.
                # It will also be added towards the missing records counter. [52]

# Records of the raw data [124] and cleaned up data [125]
num_records = num_files * len(dates) # 500 (number of files) * 365 (number of lines in a file)
cleaned_records = num_records - missing_records # Reference missing_records from [119]

# Find station with the most records.
max_records = 0 # Track maximum number of records.
for station in raw_station_data:
    record_count = len(raw_station_data[station])  # Count records for this station.
    if record_count > max_records: # replaces max_record if recorded count is bigger than the max.
        max_records = record_count
        most_records_station = station

# Task 3, Average Temperature

for station in stations:
    count = 0 # Sums up all the temps in the station [143]
    record_count = len(stations[station]) # Number of Files to go through
    if record_count > 0:
        for data in stations[station]:#Goes through the tuple to use temp to find avg_temp [142-144]
            temp = data[1] 
            count = count + temp
        avg_temp = count / record_count
        avg_temps[station] = avg_temp # Appends the avg value to the station dictionary

for station in avg_temps: # Used the above avg_temps of each station to find the highest and lowest
                          # avg_temp stations. If the avg is greater than the highest, it replaces
                          # it and vice versa.
    avg = avg_temps[station]
    if avg > highest_avg_trend:
        highest_avg_trend = float(avg)
        highest_station = station
    if avg < lowest_avg_trend:
        lowest_avg_trend = float(avg)
        lowest_station = station

# Task 4, Extreme Weather Analysis, this is essentially the same procedures as above, but instead
# it processes the station dictionary and indexes the required variable to output as a tuple.
# Data is printed via slicing [235 - 240]. 

for station in stations:
    for record in stations[station]:
        date = record[0]
        temp = record[1]
        precip = record[2]

        if temp > highest_temp:
            highest_temp = temp
            highest_temp_date = date
            highest_temp_station = station
        if temp < lowest_temp:
            lowest_temp = temp
            lowest_temp_date = date
            lowest_temp_station = station

        if precip > first_precip[0]:
            third_precip = second_precip
            second_precip = first_precip
            first_precip = (precip, date, station)

        elif precip > second_precip[0]:
            third_precip = second_precip
            second_precip = (precip, date, station)
        elif precip > third_precip[0]:
            third_precip = (precip, date, station)

# Task 5 Season Averages, indexes month [191 - 192], then indexes the temp [193-194], and calculates
# the total data and recorded temp of the file in designated season, then finds the average
# [209-213]. 
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

# If and else statements prevents dividing by 0 [209-218] which would produce an error.
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

# Print statements
# All rounding of values done here as well as removing '.csv'
print(f'\nProcessing started...\nProcessed {num_files} stations and {len(dates)} dates\n\
Total Records: {num_records}')
print(f'Station with the most records: {most_records_station.replace('.csv', '')}\n')

print(f'Records with missing temperatures: {missing_records}\nRecords remaining: {cleaned_records}')
print(f'Remaining stations after cleaning: {len(stations)}\n')

print(f'Station with the highest average temperature is: {highest_station.replace('.csv', '')}')
print(f'With the temperature of {highest_avg_trend:.2f}°C\n')
print(f'Station with the lowest average temperature is: {lowest_station.replace('.csv','')}')
print(f'With the temperature of {lowest_avg_trend:.2f}°C\n')

print('Top 3 precipitation records:')
print(f'{first_precip[1]} at Station {first_precip[2].replace('.csv', '')}:\
 {first_precip[0]:.2f} mm')
print(f'{second_precip[1]} at Station {second_precip[2].replace('.csv', '')}:\
 {second_precip[0]:.2f} mm')
print(f'{third_precip[1]} at Station {third_precip[2].replace('.csv', '')}:\
 {third_precip[0]:.2f} mm\n')

print(f'Highest Temprature: {highest_temp:.2f}°C on {highest_temp_date} at Station\
 {highest_temp_station.replace('.csv','')}')
print(f'Lowest Temprature: {lowest_temp:.2f}°C on {lowest_temp_date} at Station\
 {lowest_temp_station.replace('.csv','')}\n')

print(f'Average temperature in Winter: {winter_avg:.2f}°C\nAverage temperature in Spring:\
 {spring_avg:.2f}°C')
print(f'Average temperature in Summer: {summer_avg:.2f}°C\nAverage temperature in Fall:\
 {fall_avg:.2f}°C')
print('\nEnd of processing...\n')
