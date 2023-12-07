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

# Group data by 'Area', 'Task', and calculate average total duration
average_duration_per_task = filtered_data.groupby(['Area', 'Task'])['Duration'].mean().reset_index()

# Pivot the DataFrame for better plotting
pivot_data = average_duration_per_task.pivot(index='Area', columns='Task', values='Duration')

# Plot the data using seaborn for better color handling
sns.set_palette("husl")
pivot_data.plot(kind='bar', stacked=True, figsize=(12, 6))

# Add labels and title
plt.xlabel('Area')
plt.ylabel('Average Total Duration (minutes)')
plt.title('Average Total Duration by Area')

# Show the plot
plt.show()
