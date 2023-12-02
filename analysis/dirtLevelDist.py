import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file
df = pd.read_csv('../custodial/task_completion_log.csv')

# Plotting example for Dirt Level distribution
fig, ax = plt.subplots(figsize=(8, 6))
fig.suptitle('Distribution of Dirt Levels')

# Histogram: Dirt level distribution
df['Dirt Level'].plot(kind='hist', bins=10, color='green', edgecolor='black', ax=ax)
ax.set_xlabel('Dirt Level')
ax.set_ylabel('Frequency')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
