# # # from sklearn.experimental import enable_hist_gradient_boosting  # noqa
# # # from sklearn.ensemble import HistGradientBoostingRegressor
# # # from sklearn.pipeline import Pipeline
# # # import pandas as pd
# # # import pickle

# # # # Load and clean the data
# # # data = pd.read_csv('data/match_data.csv')
# # # data = data.dropna()  # Drop rows with NaNs if needed, or use imputation

# # # # Split features and target
# # # X = data[['HomeTeam', 'AwayTeam']]
# # # y = data[['HomeGoals', 'AwayGoals']]

# # # # Define and train the model
# # # model = HistGradientBoostingRegressor()
# # # model.fit(X, y)

# # # # Save the model
# # # with open('models/trained_model.pkl', 'wb') as f:
# # #     pickle.dump(model, f)


# # import pandas as pd
# # from sklearn.model_selection import train_test_split
# # from sklearn.preprocessing import LabelEncoder
# # from sklearn.experimental import enable_hist_gradient_boosting
# # from sklearn.ensemble import HistGradientBoostingRegressor
# # import pickle

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
# # model = HistGradientBoostingRegressor()
# # model.fit(X_train, y_train)

# # # Save the model and the label encoder
# # with open('models/trained_model.pkl', 'wb') as f:
# #     pickle.dump(model, f)

# # with open('models/label_encoder.pkl', 'wb') as f:
# #     pickle.dump(label_encoder, f)

# # print("Model and label encoder saved successfully.")


# import pandas as pd
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import LabelEncoder
# from sklearn.experimental import enable_hist_gradient_boosting
# from sklearn.ensemble import HistGradientBoostingRegressor
# import pickle

# # Load the data
# data = pd.read_csv('data/match_data.csv')

# # Encode team names using LabelEncoder
# label_encoder = LabelEncoder()
# data['HomeTeam'] = label_encoder.fit_transform(data['HomeTeam'])
# data['AwayTeam'] = label_encoder.fit_transform(data['AwayTeam'])

# # Create the feature set and the target variables
# X = data[['HomeTeam', 'AwayTeam']]
# y = data[['HomeGoals', 'AwayGoals']]

# # Split the data into training and test sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# # Train the model
# model = HistGradientBoostingRegressor()
# model.fit(X_train, y_train)

# # Save the model and the label encoder
# with open('models/trained_model.pkl', 'wb') as f:
#     pickle.dump(model, f)

# with open('models/label_encoder.pkl', 'wb') as f:
#     pickle.dump(label_encoder, f)

# print("Model and label encoder saved successfully.")


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.experimental import enable_hist_gradient_boosting
from sklearn.ensemble import HistGradientBoostingRegressor
import pickle

# Load the data
data = pd.read_csv('data/match_data.csv')

# Encode team names using LabelEncoder
label_encoder = LabelEncoder()
data['HomeTeam'] = label_encoder.fit_transform(data['HomeTeam'])
data['AwayTeam'] = label_encoder.fit_transform(data['AwayTeam'])

# Create the feature set and the target variables
X = data[['HomeTeam', 'AwayTeam']]
y_home = data['HomeGoals']
y_away = data['AwayGoals']

# Split the data into training and test sets
X_train, X_test, y_home_train, y_home_test = train_test_split(X, y_home, test_size=0.2, random_state=42)
X_train, X_test, y_away_train, y_away_test = train_test_split(X, y_away, test_size=0.2, random_state=42)

# Train the models
model_home = HistGradientBoostingRegressor()
model_home.fit(X_train, y_home_train)

model_away = HistGradientBoostingRegressor()
model_away.fit(X_train, y_away_train)

# Save the models and the label encoder
with open('models/trained_model_home.pkl', 'wb') as f:
    pickle.dump(model_home, f)

with open('models/trained_model_away.pkl', 'wb') as f:
    pickle.dump(model_away, f)

with open('models/label_encoder.pkl', 'wb') as f:
    pickle.dump(label_encoder, f)

print("Models and label encoder saved successfully.")
