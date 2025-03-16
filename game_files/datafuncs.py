"""
csv functions file
"""

import pandas as pd

# datafuncs.generate_dataframe('gamedata.csv', ['userid', 'coins', 'level'])

def generate_dataframe(filename, column_names):
    # Create an empty DataFrame with the specified column names
    df = pd.DataFrame(columns=column_names)

    # Save the DataFrame to a CSV file
    df.to_csv(filename, index=False)

    print(f'CSV file {filename} with columns {column_names} created successfully!')

def extract_data(filename):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Display the first few rows of the DataFrame
    print(df.head())

    return df

def add_data(filename, new_data):
    try:
        # Read the existing CSV file into a DataFrame
        df = pd.read_csv(filename)
    except FileNotFoundError:
        # If the file doesn't exist, start with an empty DataFrame with the columns from the new_data
        df = pd.DataFrame(columns=new_data[0].keys())

    # Convert the new data into a DataFrame
    new_df = pd.DataFrame.from_records(new_data)

    # Append the new data to the existing DataFrame
    updated_df = pd.concat([df, new_df], ignore_index=True)

    # Save the updated DataFrame back to the CSV file
    updated_df.to_csv(filename, index=False)

    print(f'New data added to {filename} successfully!')

def check_user_id(filename, user_id):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(filename)

    # Check if the User_ID exists in the DataFrame
    if user_id in df['userid'].values:
        print(f'User ID {user_id} found in {filename}.')
        return True
    else:
        print(f'User ID {user_id} not found in {filename}.')
        return False

def update_single_variable(filename, userid, variable_name, new_value):
    try:
        # Read the existing CSV file into a DataFrame
        df = pd.read_csv(filename)

        # Check if the userid exists in the DataFrame
        if userid not in df['userid'].values:
            print(f'User ID {userid} not found in {filename}.')
            return

        # Update the specified variable for the specified userid
        df.loc[df['userid'] == userid, variable_name] = new_value

        # Save the updated DataFrame back to the CSV file
        df.to_csv(filename, index=False)

        print(f'{variable_name} for User ID {userid} updated successfully!')

    except FileNotFoundError:
        print(f'The file {filename} does not exist.')
    except KeyError:
        print(f'The variable {variable_name} does not exist in the data.')

# Example usage:
# update_single_variable('userdata.csv', 1, 'coins', 100)


def update_data(filename, userid, new_coins, new_level, new_health, new_shield, new_dmgmulti, new_critchance,
                new_critmulti, new_accuracy, new_world, new_storytasks):
    try:
        # Read the existing CSV file into a DataFrame
        df = pd.read_csv(filename)

        # Check if the userid exists in the DataFrame
        if userid not in df['userid'].values:
            print(f'User ID {userid} not found in {filename}.')
            return

        # ['userid', 'coins', 'level', 'health', 'dmgmulti',
        # 'critchance', 'critmulti', 'accuracy', 'world']
        # Update the coins and level for the specified userid
        df.loc[df['userid'] == userid, 'coins'] = new_coins
        df.loc[df['userid'] == userid, 'level'] = new_level
        df.loc[df['userid'] == userid, 'health'] = new_health
        df.loc[df['userid'] == userid, 'dmgmulti'] = new_dmgmulti
        df.loc[df['userid'] == userid, 'shield'] = new_shield
        df.loc[df['userid'] == userid, 'critchance'] = new_critchance
        df.loc[df['userid'] == userid, 'critmulti'] = new_critmulti
        df.loc[df['userid'] == userid, 'accuracy'] = new_accuracy
        df.loc[df['userid'] == userid, 'world'] = new_world
        df.loc[df['userid'] == userid, 'storytasks'] = new_storytasks

        # Save the updated DataFrame back to the CSV file
        df.to_csv(filename, index=False)

        print(f'Data for User ID {userid} updated successfully!')

    except FileNotFoundError:
        print(f'The file {filename} does not exist.')

def gameupd(person):
    update_data('gamedata.csv', person.name, person.coins, person.level, person.health, person.dmgmulti,
                          person.shield, person.critchance, person.critmulti,
                          person.accuracy, person.world, person.storytasks)
