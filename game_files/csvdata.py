"""
old test code, datafuncs has the csv functions.
"""

import pandas as pd
import random
import string

# Function to generate a random 10-character user ID
def generate_user_id(existing_ids):
    characters = string.ascii_letters + string.digits
    while True:
        user_id = ''.join(random.choice(characters) for _ in range(10))
        if user_id not in existing_ids:
            return user_id

# Sample player data
player_names = ['Alice', 'Bob', 'Charlie']
player_ages = [25, 30, 35]
player_scores = [85, 95, 75]

# Collect existing IDs to ensure uniqueness
existing_ids = set()

# Create player data with unique UserIDs
player_data = {
    'Name': player_names,
    'Age': player_ages,
    'Score': player_scores,
    'UserID': [generate_user_id(existing_ids) for _ in range(len(player_names))]
}

# Add generated user IDs to the existing IDs set
existing_ids.update(player_data['UserID'])

# Create a DataFrame
df = pd.DataFrame(player_data)

# Save the DataFrame to a CSV file
df.to_csv('player_data.csv', index=False)

print("Player data saved to 'player_data.csv'")
