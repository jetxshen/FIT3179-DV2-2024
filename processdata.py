import pandas as pd

# Load the dataset
anime_data = pd.read_csv('animes.csv')

# Split the 'genre' column and explode into multiple rows
anime_data['genre'] = anime_data['genre'].apply(lambda x: eval(x))  # Convert string list to actual list
genre_exploded = anime_data.explode('genre')  # Split genres into separate rows

# Save the processed data to a new CSV
genre_exploded.to_csv('processed_genre_data.csv', index=False)