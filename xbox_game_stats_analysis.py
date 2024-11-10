#import necessary libraries
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the CSV file
df = pd.read_csv("Final Raw Data Xbox Stats.csv")

# Convert 'Percent Complete' to float
df['Percent Complete'] = df['Percent Complete'].astype(str).str.replace('%', '').astype(float)

# Filter games with achievement percentage greater than 50
percent_filter = df.query('`Percent Complete` > 50')
genre_filter = percent_filter['Genre']

colors1 = plt.cm.viridis(np.linspace(0, 1, len(genre_filter)))

# Plot graph for games with over 50% completion
genre_filter.value_counts().plot(kind='bar', figsize=(10, 6), color=colors1)
plt.xticks(rotation=45, ha='right')
plt.title('Distribution of Game Genres with Over 50% Completion')
plt.xlabel('Genre')
plt.ylabel('Count of Games')
plt.tight_layout()
plt.show()

# Count the number of occurrences in the genre filter
genre_counts = percent_filter['Genre'].value_counts()

# Condense similar genres into one category to display data clearer
genre_mapping = {
    'First-person shooter': 'Shooter',
    'Shooter': 'Shooter',
    'Action RPG': 'Action',
    'Action-Adventure': 'Action',
    'Action-Adventure / Puzzle': 'Action',
    'Action-Adventure / RPG': 'Action',
    'Action / Fighting': 'Action',
    'Action / Platformer': 'Action',
    'Sports': 'Sports',
    'Sports / Fighting': 'Sports',
    'Battle Royale': 'Battle Royale',
    'Survival Horror': 'Horror',
    'Party Game': 'Party',
    'RPG': 'RPG',
    'Fighting': 'Fighting',
    'Platformer': 'Platformer',
    'Simulation': 'Simulation',
    'Sandbox': 'Sandbox',
    'Racing': 'Racing',
    'Music': 'Music',
    'Adventure / Mystery': 'Mystery',
    'Tower Defense / RPG': 'RPG',
}

# Replace genres with the simplified version
df['Genre'] = df['Genre'].replace(genre_mapping)

# Count each value in the Genre column
genre_counts = df['Genre'].value_counts()

# Color the graph
colors = plt.cm.viridis(np.linspace(0, 1, len(genre_counts)))

# Plot graph for all games
genre_counts.plot(kind='bar', figsize=(10, 6), color=colors)
plt.xticks(rotation=45, ha='right')
plt.title('Distribution of Game Genres')
plt.ylabel('Count of Games')
plt.tight_layout()
plt.show()

# Close all figures to free up memory
plt.close('all')

# Get all games with 100% completion
max_complete_games = df[df['Percent Complete'] == 100]['Game']
# Get all games with the lowest completion
min_complete_games = df[df['Percent Complete'] <= 1]['Game']

# Retrieve more descriptive statistics
most_common_genre = genre_counts.idxmax()
highest_count = genre_counts.max()

# Display results
print(f"The genre with the highest count of games is {most_common_genre} with {highest_count} games!")
print()
print(f"The genre that has the most games with more than 50% completion is: {most_common_genre}")
print()
print(f"The game(s) with 100% completion are: {', '.join(max_complete_games)}")
print()
print(f"The game(s) with at least 1% completion are: {', '.join(min_complete_games)}")
