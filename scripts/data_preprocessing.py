# # # # import pandas as pd

# # # # def preprocess_data(input_path, output_path):
# # # #     # Load the dataset
# # # #     data = pd.read_csv(input_path)

# # # #     # Select relevant columns and handle missing values
# # # #     data = data[['HomeTeam', 'AwayTeam', 'HomeGoals', 'AwayGoals']]
# # # #     data = data.dropna()

# # # #     # Encode categorical variables
# # # #     data['Home_team'] = data['Home_team'].astype('category').cat.codes
# # # #     data['Away_team'] = data['Away_team'].astype('category').cat.codes

# # # #     # Rename columns for consistency
# # # #     data.rename(columns={'HomeTeam': 'HomeTeam', 'AwayTeam': 'AwayTeam'}, inplace=True)

# # # #     # Save the preprocessed data
# # # #     data.to_csv(output_path, index=False)

# # # # if __name__ == "__main__":
# # # #     preprocess_data('data/match_data.csv', 'data/preprocessed_data.csv')

# # # def preprocess_input(home_team, away_team):
# # #     # Load the preprocessed data to get encoding mappings
# # #     preprocessed_data = pd.read_csv('data/preprocessed_data.csv')
# # #     team_encodings = preprocessed_data[['HomeTeam', 'AwayTeam']].drop_duplicates().reset_index(drop=True)
# # #     team_mapping = dict(zip(team_encodings['HomeTeam'], team_encodings.index))

# # #     # Create a DataFrame with the input data
# # #     data = pd.DataFrame({
# # #         'HomeTeam': [home_team],
# # #         'AwayTeam': [away_team]
# # #     })

# # #     # Encoding teams
# # #     data['HomeTeam'] = data['HomeTeam'].map(team_mapping)
# # #     data['AwayTeam'] = data['AwayTeam'].map(team_mapping)

# # #     # Add GoalDifference column for consistency
# # #     data['GoalDifference'] = 0  # Placeholder if used during training

# # #     # Handle missing values
# # #     data = data.fillna(0)  # Or use a different strategy if needed

# # #     # Debugging: Print the preprocessed input data
# # #     print("Preprocessed Input Data:\n", data)

# # #     return data[['HomeTeam', 'AwayTeam', 'GoalDifference']]


# # import pandas as pd
# # from sklearn.model_selection import train_test_split
# # from sklearn.preprocessing import LabelEncoder

# # # Load the data
# # data = pd.read_csv('data/match_data.csv')

# # # Encode team names using LabelEncoder
# # label_encoder = LabelEncoder()
# # data['HomeTeam'] = label_encoder.fit_transform(data['HomeTeam'])
# # data['AwayTeam'] = label_encoder.fit_transform(data['AwayTeam'])

# # # Create the feature set and the target variables
# # X = data[['HomeTeam', 'AwayTeam']]
# # y = data[['HomeGoals', 'AwayGoals']]

# # # Split the data into training and test sets
# # X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # # Train the model
# # from sklearn.experimental import enable_hist_gradient_boosting
# # from sklearn.ensemble import HistGradientBoostingRegressor
# # import pickle

# # model = HistGradientBoostingRegressor()
# # model.fit(X_train, y_train)

# # # Save the model and the label encoder
# # with open('models/trained_model.pkl', 'wb') as f:
# #     pickle.dump(model, f)

# # with open('models/label_encoder.pkl', 'wb') as f:
# #     pickle.dump(label_encoder, f)

# import pandas as pd
# import pickle

# def load_label_encoder():
#     with open('models/label_encoder.pkl', 'rb') as f:
#         return pickle.load(f)

# def preprocess_input(home_team, away_team):
#     # Load the label encoder
#     label_encoder = load_label_encoder()

#     # Create a DataFrame with the input data
#     data = pd.DataFrame({
#         'HomeTeam': [home_team],
#         'AwayTeam': [away_team]
#     })

#     # Encoding teams using the loaded label encoder
#     data['HomeTeam'] = label_encoder.transform(data['HomeTeam'])
#     data['AwayTeam'] = label_encoder.transform(data['AwayTeam'])

#     return data[['HomeTeam', 'AwayTeam']]


import pandas as pd
import pickle

def load_label_encoder():
    with open('models/label_encoder.pkl', 'rb') as f:
        return pickle.load(f)

def preprocess_input(home_team, away_team):
    # Load the label encoder
    label_encoder = load_label_encoder()

    # Create a DataFrame with the input data
    data = pd.DataFrame({
        'HomeTeam': [home_team],
        'AwayTeam': [away_team]
    })

    # Encoding teams using the loaded label encoder
    data['HomeTeam'] = label_encoder.transform(data['HomeTeam'])
    data['AwayTeam'] = label_encoder.transform(data['AwayTeam'])

    return data[['HomeTeam', 'AwayTeam']]
