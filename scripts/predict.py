import pandas as pd
import pickle

def preprocess_input(home_team, away_team):
    # Load the preprocessed data to get encoding mappings
    preprocessed_data = pd.read_csv('data/preprocessed_data.csv')
    team_encodings = preprocessed_data[['HomeTeam', 'AwayTeam']].drop_duplicates().reset_index(drop=True)
    team_mapping = dict(zip(team_encodings['HomeTeam'], team_encodings.index))

    # Create a DataFrame with the input data
    data = pd.DataFrame({
        'HomeTeam': [home_team],
        'AwayTeam': [away_team]
    })

    # Encoding teams
    data['HomeTeam'] = data['HomeTeam'].map(team_mapping)
    data['AwayTeam'] = data['AwayTeam'].map(team_mapping)

    # Add GoalDifference column for consistency
    data['GoalDifference'] = 0  # Placeholder if used during training

    # Handle missing values
    data = data.fillna(0)  # Or use a different strategy if needed

    return data[['HomeTeam', 'AwayTeam', 'GoalDifference']]

def make_prediction(home_team, away_team):
    # Preprocess the input
    input_data = preprocess_input(home_team, away_team)

    # Load the model
    with open('models/trained_model.pkl', 'rb') as f:
        model = pickle.load(f)

    # Make prediction
    predictions = model.predict(input_data)

    # Output the predictions
    print(f"Predicted Home Goals: {predictions[0][0]}")
    print(f"Predicted Away Goals: {predictions[0][1]}")

if __name__ == "__main__":
    # Example input
    home_team = 'Manchester United'
    away_team = 'Arsenal'

    make_prediction(home_team, away_team)
