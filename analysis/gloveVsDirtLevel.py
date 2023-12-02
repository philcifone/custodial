import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('task_completion_log.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Create subplots
fig, ax = plt.subplots(figsize=(10, 6))
fig.suptitle('Daily Gloves Used vs Daily Average Dirt Level')

# Line plot: Daily gloves used
df.groupby(df['Date'].dt.strftime('%Y-%m-%d'))['Gloves'].sum().plot(ax=ax, kind='line', marker='o', color='blue', label='Gloves Used')

# Bar plot: Daily average dirt level
df.groupby(df['Date'].dt.strftime('%Y-%m-%d'))['Dirt Level'].mean().plot(ax=ax, kind='bar', color='orange', alpha=0.7, label='Average Dirt Level')

# Set labels and legend
ax.set_xlabel('Date')
ax.set_ylabel('Count / Level')
ax.legend()

# Adjust layout for better appearance
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()
