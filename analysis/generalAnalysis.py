import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('../custodial/task_completion_log.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Convert the 'Duration' column to timedelta
df['Duration'] = pd.to_timedelta(df['Duration'])

# Get the order of sections based on the minimum 'Task Number'
#section_order = df.groupby('Section')['Task Number'].min().sort_values().index

# Plotting examples
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
fig.suptitle('Section Analysis')

# Plot 1: Average duration of tasks per section
df['Duration'] = pd.to_timedelta(df['Duration'])
df.groupby('Section')['Duration'].mean().dt.total_seconds().div(60).plot(ax=axes[0, 0], kind='bar', color='blue')
axes[0, 0].set_title('Average Duration of Tasks per Section')
axes[0, 0].set_xlabel('Section')
axes[0, 0].set_ylabel('Time in minutes')

# Plot 2b: Dirt levels per task
df.groupby('Section')['Dirt Level'].mean().plot(ax=axes[1, 0], kind='bar', color='green')
axes[1, 0].set_title('Dirt Levels per Task')
axes[1, 0].set_xlabel('Section')
axes[1, 0].set_ylabel('Dirt Level')
#axes[1, 0].tick_params(axis='x', rotation=90)

# Plot 3: Duration per square foot per section
# Calculate duration per square foot
df['Duration_per_sqft'] = df['Duration'] / df['Size']

# Convert Timedelta to seconds
df['Duration_per_sqft'] = df['Duration_per_sqft'].dt.total_seconds()
# Actual Plot
df.groupby('Section')['Duration_per_sqft'].mean().plot(kind='bar', ax=axes[0, 1], color='orange', legend=False)
axes[0, 1].set_title(f'Average Duration per Square Foot per Section')
axes[0, 1].set_xlabel('Section')
axes[0, 1].set_ylabel('Time in minutes')

# Plot 4: Total gloves used per day
df.groupby(df['Date'].dt.strftime('%Y-%m-%d'))['Gloves'].sum().plot(kind='bar', color='purple', ax=axes[1, 1])
axes[1, 1].set_title('Pairs of Gloves Used Each Day')
axes[1, 1].set_xlabel('Date')
axes[1, 1].set_ylabel('Total Gloves Used')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()