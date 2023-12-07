import pandas as pd
import matplotlib.pyplot as plt

# Replace 'your_existing_data.csv' with your actual CSV file path
data = pd.read_csv('task_completion_log.csv')

# Extract relevant columns
relevant_columns = ['Area', 'Task', 'Size', 'Duration']
filtered_data = data[relevant_columns]

# Convert 'Duration' to seconds for easier analysis
filtered_data['Duration'] = pd.to_timedelta(filtered_data['Duration']).dt.total_seconds()

# Group data by 'Area', 'Task', and calculate average duration per square foot
average_duration_per_task = filtered_data.groupby(['Area', 'Task']).mean()

# Reset index for better plotting
average_duration_per_task = average_duration_per_task.reset_index()

# Plot the data
for task in average_duration_per_task['Task'].unique():
    task_data = average_duration_per_task[average_duration_per_task['Task'] == task]
    plt.bar(task_data['Area'], task_data['Duration'] / task_data['Size'], label=task)

# Add labels and legend
plt.xlabel('Area')
plt.ylabel('Average Duration per Square Foot')
plt.title('Average Duration per Square Foot per Task')
plt.legend(title='Task', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()
