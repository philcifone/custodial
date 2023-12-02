import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('task_completion_log.csv')

# Convert the 'Duration' column to timedelta
df['Duration'] = pd.to_timedelta(df['Duration'])

# Calculate total square footage cleaned per day
df['Total_Sqft'] = df['Size'].groupby(df['Date']).transform('sum')

# Plotting example
fig, ax1 = plt.subplots(figsize=(12, 6))

# Bar graph: Total square footage cleaned per day
df.groupby('Date')['Total_Sqft'].max().plot(ax=ax1, kind='bar', color='blue', alpha=0.5, label='Total Square Footage Cleaned')
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Square Footage Cleaned', color='blue')
ax1.legend(loc='upper left')

# Create a secondary y-axis for the line graph
ax2 = ax1.twinx()

# Line graph: Average duration per task
df.groupby('Date')['Duration'].mean().dt.total_seconds().div(60).plot(ax=ax2, kind='line', marker='o', color='orange', label='Average Task Duration')
ax2.set_ylabel('Average Task Duration (minutes)', color='orange')

ax2.legend(loc='upper right')

# Adjust layout for better appearance
plt.title('Comparison of Average Task Duration and Total Square Footage Cleaned per Day')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()
