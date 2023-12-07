import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Replace 'your_existing_data.csv' with your actual CSV file path
data = pd.read_csv('task_completion_log.csv')

# Extract relevant columns
relevant_columns = ['Area', 'Task', 'Duration']
filtered_data = data[relevant_columns]

# Convert 'Duration' to minutes for easier analysis
filtered_data['Duration'] = pd.to_timedelta(filtered_data['Duration']).dt.total_seconds() / 60

# Group data by 'Area' and 'Task', and calculate total duration
total_duration_per_task = filtered_data.groupby(['Area', 'Task']).sum()

# Reset index for better plotting
total_duration_per_task = total_duration_per_task.reset_index()

# Pivot the DataFrame for better plotting
pivot_data = total_duration_per_task.pivot(index='Area', columns='Task', values='Duration')

# Plot the data using seaborn for better color handling
sns.set_palette("husl")
pivot_data.plot(kind='bar', stacked=True, figsize=(12, 6))

# Add labels and legend
plt.xlabel('Area')
plt.ylabel('Total Duration in Minutes')
plt.title('Total Duration of Each Task per Area')
plt.legend(title='Task', bbox_to_anchor=(1, 1))

# Show the plot
plt.show()
