import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('task_completion_log.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Convert the 'Duration' column to timedelta
df['Duration'] = pd.to_timedelta(df['Duration'])

# Get the order of sections based on the minimum 'Task Number'
section_order = df.groupby('Section')['Task Number'].min().sort_values().index

# Plotting examples
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
fig.suptitle('Daily Task Completion Analysis')

# Plot 1: Task completion count per day
df['Date'].value_counts().sort_index().plot(ax=axes[0, 0], kind='bar', color='skyblue')
axes[0, 0].set_title('Task Completion Count per Day')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Count')

# Plot 2: Average duration of tasks per day
df.groupby('Date')['Duration'].mean().dt.total_seconds().div(60).plot(ax=axes[1, 1], kind='line', marker='o', color='orange')
axes[1, 1].set_title('Average Duration of Tasks per Day (minutes)')
axes[1, 1].set_xlabel('Date')
axes[1, 1].set_ylabel('Average Duration')

#Plot 2
#df['Duration_minutes'] = df['Duration'].dt.total_seconds() / 60
#df.plot(x='Section', y='Duration_minutes', kind='bar', ax=axes[0, 0], color='skyblue', legend=False)
#axes[0, 0].set_title(f'Duration of Tasks per Day - {csv_date}')
#axes[0, 0].set_xlabel('Section')
#axes[0, 0].set_ylabel('Duration (minutes)')

# Plot 3: Dirt level distribution
df['Dirt Level'].plot(ax=axes[1, 0], kind='hist', bins=10, color='green', edgecolor='black')
axes[1, 0].set_title('Distribution of Dirt Levels')
axes[1, 0].set_xlabel('Dirt Level')
axes[1, 0].set_ylabel('Frequency')

# Plot 3: Dirt levels per task
#df.plot(x='Section', y='Dirt Level', kind='bar', ax=axes[1, 0], color='green', legend=False)
#axes[1, 0].set_title(f'Dirt Levels per Task - {csv_date}')
#axes[1, 0].set_xlabel('Section')
#axes[1, 0].set_ylabel('Dirt Level')

# Plot 5: Duration per square foot per section
# Calculate duration per square foot
df['Duration_per_sqft'] = df['Duration'] / df['Size']

# Convert Timedelta to seconds
df['Duration_per_sqft'] = df['Duration_per_sqft'].dt.total_seconds()
# Actual Plot
df.groupby('Section')['Duration_per_sqft'].mean().loc[section_order].plot(kind='bar', ax=axes[0, 1], color='orange', legend=False)
axes[0, 1].set_title(f'Average Duration per Square Foot per Section')
axes[0, 1].set_xlabel('Section')
axes[0, 1].set_ylabel('Average Duration per Square Foot')
#axes[0, 1].tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better visibility

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()