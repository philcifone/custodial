import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('../custodial/task_completion_log.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set the order of Areas based on the minimum 'Task Number'
Area_order = df.groupby('Area')['Task Number'].min().sort_values().index

# Plotting example for Average Duration of Tasks per Area
fig, ax = plt.subplots(figsize=(8, 6))
fig.suptitle('Daily Task Completion Analysis')

df['Duration'] = pd.to_timedelta(df['Duration'])
df.groupby('Area')['Duration'].mean().dt.total_seconds().div(60).loc[Area_order].plot(ax=ax, kind='bar', color='orange')
ax.set_title('Average Duration of Tasks per Area (minutes)')
ax.set_xlabel('Area')
ax.set_ylabel('Average Duration')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
