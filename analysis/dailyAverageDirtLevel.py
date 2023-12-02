import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('../custodial/task_completion_log.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Plotting example for Daily Average Dirt Level (Bar Graph)
fig, ax = plt.subplots(figsize=(10, 6))
fig.suptitle('Daily Average Dirt Level')

# Bar Plot: Daily average dirt level
df.groupby(df['Date'].dt.strftime('%Y-%m-%d'))['Dirt Level'].mean().plot(kind='bar', color='green', ax=ax)
ax.set_xlabel('Date')
ax.set_ylabel('Average Dirt Level')

# Adjust layout for better appearance
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
