import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('task_completion_log.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Extract the day of the week and create a new column
df['DayOfWeek'] = df['Date'].dt.day_name()

# Plotting example
fig, ax = plt.subplots(figsize=(10, 6))
fig.suptitle('Average Dirt Levels by Day of Week')

# Plot: Average dirt levels by day of week
df.groupby('DayOfWeek')['Dirt Level'].mean().plot(kind='bar', color='green', ax=ax)
ax.set_xlabel('Day of Week')
ax.set_ylabel('Average Dirt Level')

plt.show()
