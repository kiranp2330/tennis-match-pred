import pandas as pd

# Load dataset
data = pd.read_csv('data/tennis_matches.csv')

# Drop rows with missing values in critical columns
data = data.dropna(subset=['ServePointsWon', 'ReturnPointsWon', 'Aces', 'DoubleFaults'])

# Feature Engineering
data['ServeEfficiency'] = data['Aces'] - data['DoubleFaults']

# One-Hot Encoding for categorical features
data = pd.get_dummies(data, columns=['Surface', 'TournamentLevel'])

# Save cleaned data
data.to_csv('data/cleaned_tennis_matches.csv', index=False)
print("Data cleaning complete. Saved to 'data/cleaned_tennis_matches.csv'.")
