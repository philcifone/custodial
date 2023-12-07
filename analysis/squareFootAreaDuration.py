import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('../custodial/task_completion_log.csv')

# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Set variable for date
csv_date = df['Date'].max().strftime("%Y-%m-%d")

# Set the order of Areas based on the minimum 'Task Number'
Area_order = df.groupby('Area')['Task Number'].min().sort_values().index

# Plotting example for Average Duration per Square Foot
fig, ax = plt.subplots(figsize=(8, 6))
df['Duration'] = pd.to_timedelta(df['Duration'])
df['Duration_per_sqft'] = df['Duration'] / df['Size']
df['Duration_per_sqft'] = df['Duration_per_sqft'].dt.total_seconds()
df.groupby('Area')['Duration_per_sqft'].mean().loc[Area_order].plot(kind='bar', color='orange', ax=ax)
ax.set_title(f'Average Duration per Square Foot per Area')
ax.set_xlabel('Area')
ax.set_ylabel('Average Duration per Square Foot')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
