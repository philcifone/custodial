import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('task_completion_log.csv')

# Convert Duration to timedelta
df['Duration'] = pd.to_timedelta(df['Duration'])

# Create a grouped bar chart
grouped_df = df.groupby(['Area', 'Task'])['Duration'].mean().dt.total_seconds().div(60).unstack()


# Duration per square foot per Task
# Calculate duration per square foot
df['Duration_per_sqft'] = df['Duration'] / df['Size']

# Convert Timedelta to seconds
df['Duration_per_sqft'] = df['Duration_per_sqft'].dt.total_seconds()
# Actual Plot
df.groupby('Task')['Duration_per_sqft'].mean().plot(kind='bar', color='orange', legend=False)
plt.title('Average Duration per Square Foot per Task')
plt.xlabel('Task')
plt.ylabel('Time in Seconds')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()