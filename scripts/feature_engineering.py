import pandas as pd

def feature_engineering(input_path, features_path, target_path):
    # Load the preprocessed data
    data = pd.read_csv(input_path)

    # Add new features (e.g., GoalDifference)
    data['GoalDifference'] = data['HomeGoals'] - data['AwayGoals']

    # Define features and target variable
    features = ['HomeTeam', 'AwayTeam', 'GoalDifference']
    X = data[features]
    y = data[['HomeGoals', 'AwayGoals']]

    # Save features and target
    X.to_csv(features_path, index=False)
    y.to_csv(target_path, index=False)

if __name__ == "__main__":
    feature_engineering('data/preprocessed_data.csv', 'data/features.csv', 'data/target.csv')
