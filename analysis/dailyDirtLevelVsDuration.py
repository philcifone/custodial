import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Load the data from the CSV file
df = pd.read_csv('../custodial/task_completion_log.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Convert the 'Duration' column to timedelta
df['Duration'] = pd.to_timedelta(df['Duration'])

# Plotting example
fig, ax1 = plt.subplots(figsize=(10, 6))
fig.suptitle('Daily Duration and Dirt Levels')

# Plot 1: Daily average task duration
df.groupby(df['Date'].dt.strftime('%Y-%m-%d'))['Duration'].mean().dt.total_seconds().div(60).plot(kind='bar', color='orange', ax=ax1, label='Duration')
ax1.set_xlabel('Date')
ax1.set_ylabel('Average Task Duration (minutes)', color='orange')
ax1.tick_params(axis='y', labelcolor='orange')

# Create a second y-axis for dirt levels
ax2 = ax1.twinx()
df.groupby(df['Date'].dt.strftime('%Y-%m-%d'))['Dirt Level'].mean().plot(kind='line', marker='o', color='green', ax=ax2, label='Dirt Level')
ax2.set_ylabel('Average Dirt Level', color='green')
ax2.tick_params(axis='y', labelcolor='green')

# Adjust layout for better appearance
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

# Show legend for both y-axes
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

plt.show()
