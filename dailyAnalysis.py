import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the data from the CSV file
df = pd.read_csv('task_completion_log.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Convert the 'Duration' column to timedelta
df['Duration'] = pd.to_timedelta(df['Duration'])

# Plotting examples
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
fig.suptitle('Daily Task Completion Analysis')

# Plot 1: Task completion count per day
#df['Date'].value_counts().sort_index().plot(ax=axes[0, 0], kind='bar', color='skyblue')
#axes[0, 0].set_title('Task Completion Count per Day')
#axes[0, 0].set_xlabel('Date')
#axes[0, 0].set_ylabel('Count')

# Plot 2: Average duration of tasks per day
#df.groupby('Date')['Duration'].mean().dt.total_seconds().div(60).plot(ax=axes[0, 1], kind='line', marker='o', color='orange')
#axes[0, 1].set_title('Average Duration of Tasks per Day (minutes)')
#axes[0, 1].set_xlabel('Date')
#axes[0, 1].set_ylabel('Average Duration')
df['Duration_minutes'] = df['Duration'].dt.total_seconds() / 60
df.plot(x='Section', y='Duration_minutes', kind='bar', ax=axes[0, 0], color='skyblue', legend=False)
axes[0, 0].set_title('Duration of Tasks per Day')
axes[0, 0].set_xlabel('Section')
axes[0, 0].set_ylabel('Duration (minutes)')

# Plot 3: Dirt level distribution
#df['Dirt Level'].plot(ax=axes[1, 0], kind='hist', bins=10, color='green', edgecolor='black')
#axes[1, 0].set_title('Distribution of Dirt Levels')
#axes[1, 0].set_xlabel('Dirt Level')
#axes[1, 0].set_ylabel('Frequency')
# Plot 3: Dirt levels per task
df.plot(x='Section', y='Dirt Level', kind='bar', ax=axes[1, 0], color='green', legend=False)
axes[1, 0].set_title('Dirt Levels per Task')
axes[1, 0].set_xlabel('Section')
axes[1, 0].set_ylabel('Dirt Level')

# Plot 4: Gloves used per task
#df['Gloves'].plot(ax=axes[1, 1], kind='box', vert=False, color='purple')
#axes[1, 1].set_title('Distribution of Gloves Used per Task')
#axes[1, 1].set_xlabel('Number of Gloves')
df.plot(x='Section', y='Gloves', kind='bar', ax=axes[1, 1], color='purple', legend=False)
axes[1, 1].set_title('Gloves Used per Task')
axes[1, 1].set_xlabel('Section')
axes[1, 1].set_ylabel('Number of Gloves')

# Plot 5: Duration per square foot per section
# Calculate duration per square foot
df['Duration_per_sqft'] = df['Duration'] / df['Size']

# Convert Timedelta to seconds
df['Duration_per_sqft'] = df['Duration_per_sqft'].dt.total_seconds()
# Actual Plot
df.groupby('Section')['Duration_per_sqft'].mean().plot(kind='bar', ax=axes[0, 1], color='orange', edgecolor='black')
axes[0, 1].set_title('Average Duration per Square Foot per Section')
axes[0, 1].set_xlabel('Section')
axes[0, 1].set_ylabel('Average Duration per Square Foot')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
