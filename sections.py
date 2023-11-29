import csv
import datetime

# Function to log task completion time
#def log_task_completion(section, task_number, start_time, end_time):
#    duration = end_time - start_time
#    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#    with open('task_completion_log.csv', 'a', newline='') as csvfile:
#        fieldnames = ['Timestamp', 'Section', 'Task Number', 'Start Time', 'End Time', 'Duration']
#        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#        if csvfile.tell() == 0:  # Write header only if the file is empty
#            writer.writeheader()
#        writer.writerow({
#            'Timestamp': timestamp,
#            'Section': section,
#            'Task Number': task_number,
#            'Start Time': start_time.strftime('%H:%M:%S'),
#            'End Time': end_time.strftime('%H:%M:%S'),
#            'Duration': str(duration)
#        })

# Example usage
#section = 'Boys Bathroom'
#start_time_1 = datetime.datetime.now()
# Perform cleaning task 1
#end_time_1 = datetime.datetime.now()
#log_task_completion(section, 1, start_time_1, end_time_1)

# Perform cleaning task 2
#start_time_2 = datetime.datetime.now()
# Perform cleaning task 2
#end_time_2 = datetime.datetime.now()
#log_task_completion(section, 2, start_time_2, end_time_2)

# ... Continue for other tasks

# Analysis: Correlation of task completion times
import pandas as pd
import matplotlib.pyplot as plt

# Read the data into a Pandas DataFrame
task_completion_data = pd.read_csv('task_completion_log.csv')

# Function to convert duration strings to seconds
def convert_duration_to_seconds(duration_str):
    parts = duration_str.split(':')
    return int(parts[0]) * 3600 + int(parts[1]) * 60 + float(parts[2])

# Convert 'Duration' column to numeric (seconds)
task_completion_data['Duration'] = task_completion_data['Duration'].apply(convert_duration_to_seconds)

# Group by task number and calculate the average duration for each task
average_duration_per_task = task_completion_data.groupby('Task Number')['Duration'].mean()

# Group by task number and calculate the average duration for each task
average_duration_per_task = task_completion_data.groupby('Task Number')['Duration'].mean()

# Plotting the average duration for each task
plt.bar(average_duration_per_task.index, average_duration_per_task)
plt.xlabel('Task Number')
plt.ylabel('Average Duration (minutes)')
plt.title('Average Duration for Each Task')
plt.show()
