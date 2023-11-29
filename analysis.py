import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('task_completion_log.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Convert the 'Duration' column to timedelta
df['Duration'] = pd.to_timedelta(df['Duration'])

# Plotting examples
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(12, 8))
fig.suptitle('Task Completion Analysis')

# Plot 1: Task completion count per day
df['Date'].value_counts().sort_index().plot(ax=axes[0, 0], kind='bar', color='skyblue')
axes[0, 0].set_title('Task Completion Count per Day')
axes[0, 0].set_xlabel('Date')
axes[0, 0].set_ylabel('Count')

# Plot 2: Average duration of tasks per day
df.groupby('Date')['Duration'].mean().dt.total_seconds().div(60).plot(ax=axes[0, 1], kind='line', marker='o', color='orange')
axes[0, 1].set_title('Average Duration of Tasks per Day (minutes)')
axes[0, 1].set_xlabel('Date')
axes[0, 1].set_ylabel('Average Duration')

# Plot 3: Dirt level distribution
df['Dirt Level'].plot(ax=axes[1, 0], kind='hist', bins=10, color='green', edgecolor='black')
axes[1, 0].set_title('Distribution of Dirt Levels')
axes[1, 0].set_xlabel('Dirt Level')
axes[1, 0].set_ylabel('Frequency')

# Plot 4: Gloves used per task
df['Gloves'].plot(ax=axes[1, 1], kind='box', vert=False, color='purple')
axes[1, 1].set_title('Distribution of Gloves Used per Task')
axes[1, 1].set_xlabel('Number of Gloves')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
