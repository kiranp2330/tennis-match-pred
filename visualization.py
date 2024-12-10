import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load cleaned data
data = pd.read_csv('data/cleaned_tennis_matches.csv')

# Visualize Serve Points Won vs Return Points Won
plt.figure(figsize=(10, 6))
sns.scatterplot(data=data, x='ServePointsWon', y='ReturnPointsWon', hue='Winner')
plt.title('Serve Points Won vs Return Points Won')
plt.xlabel('Serve Points Won (%)')
plt.ylabel('Return Points Won (%)')
plt.legend(title='Winner')
plt.grid(True)
plt.savefig('images/serve_vs_return_points.png', dpi=300)
plt.show()
