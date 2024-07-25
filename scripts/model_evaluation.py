import pandas as pd
from sklearn.metrics import mean_squared_error
import pickle
from sklearn.model_selection import train_test_split

def evaluate_model(features_path, target_path, model_path):
    # Load features and target variable
    X = pd.read_csv(features_path)
    y = pd.read_csv(target_path)

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Load the model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Predict on the test set
    y_pred = model.predict(X_test)

    # Calculate Mean Squared Error
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error: {mse}')

if __name__ == "__main__":
    evaluate_model('data/features.csv', 'data/target.csv', 'models/trained_model.pkl')
