import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('task_completion_log.csv')

# Convert Duration to timedelta
df['Duration'] = pd.to_timedelta(df['Duration'])

# Create a grouped bar chart
grouped_df = df.groupby(['Area', 'Task'])['Duration'].mean().dt.total_seconds().div(60).unstack()

# Plotting
grouped_df.plot(kind='bar', stacked=True, figsize=(10, 6), colormap='viridis')
plt.title('Average Duration of Tasks per Area (Stacked)')
plt.xlabel('Area')
plt.ylabel('Time in minutes')
plt.legend(title='Task', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

