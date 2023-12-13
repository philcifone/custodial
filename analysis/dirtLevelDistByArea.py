import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('../custodial/task_completion_log.csv')

# Group by 'Area' and calculate the average dirt level for each area
average_dirt_by_area = df.groupby('Area')['Dirt Level'].mean()

# Plotting the bar graph
plt.bar(average_dirt_by_area.index, average_dirt_by_area)
plt.xlabel('Area')
plt.ylabel('Average Dirt Level')
plt.title('Average Dirt Level by Area')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
