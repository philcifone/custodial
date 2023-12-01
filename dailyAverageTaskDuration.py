import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

# Load the data from the CSV file
df = pd.read_csv('task_completion_log.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Convert the 'Duration' column to timedelta
df['Duration'] = pd.to_timedelta(df['Duration'])

# Plotting example
fig, ax = plt.subplots(figsize=(10, 6))
fig.suptitle('Daily Average Task Duration')

# Bar Plot: Daily average task duration
df.groupby(df['Date'].dt.strftime('%Y-%m-%d'))['Duration'].mean().dt.total_seconds().div(60).plot(kind='bar', color='orange', ax=ax)
ax.set_xlabel('Date')
ax.set_ylabel('Average Task Duration (minutes)')

# Adjust layout for better appearance
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()
