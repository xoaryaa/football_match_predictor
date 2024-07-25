# # # from flask import Flask, render_template, request
# # # import pandas as pd
# # # import pickle

# # # app = Flask(__name__)

# # # # Load the model
# # # with open('models/trained_model.pkl', 'rb') as f:
# # #     model = pickle.load(f)

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

# # #     return data[['HomeTeam', 'AwayTeam', 'GoalDifference']]

# # # @app.route('/', methods=['GET', 'POST'])
# # # def index():
# # #     prediction = None
# # #     if request.method == 'POST':
# # #         home_team = request.form.get('home_team')
# # #         away_team = request.form.get('away_team')

# # #         if not home_team or not away_team:
# # #             return render_template('index.html', prediction='Invalid input. Please provide both home and away teams.')

# # #         input_data = preprocess_input(home_team, away_team)

# # #         # Make prediction
# # #         predictions = model.predict(input_data)

# # #         home_goals_pred = predictions[0][0]
# # #         away_goals_pred = predictions[0][1]

# # #         return render_template('index.html', prediction=(home_goals_pred, away_goals_pred))

# # #     return render_template('index.html', prediction=None)

# # # if __name__ == '__main__':
# # #     app.run(debug=True)


# # from flask import Flask, render_template, request
# # import pandas as pd
# # import pickle
# # from data_preprocessing import preprocess_input

# # app = Flask(__name__)

# # # Load the model
# # with open('models/trained_model.pkl', 'rb') as f:
# #     model = pickle.load(f)

# # @app.route('/', methods=['GET', 'POST'])
# # def index():
# #     prediction = None
# #     if request.method == 'POST':
# #         home_team = request.form.get('home_team')
# #         away_team = request.form.get('away_team')

# #         if not home_team or not away_team:
# #             return render_template('index.html', prediction='Invalid input. Please provide both home and away teams.')

# #         try:
# #             input_data = preprocess_input(home_team, away_team)

# #             # Make prediction
# #             predictions = model.predict(input_data)

# #             home_goals_pred = predictions[0][0]
# #             away_goals_pred = predictions[0][1]

# #             return render_template('index.html', prediction=(home_goals_pred, away_goals_pred))
# #         except ValueError as e:
# #             return render_template('index.html', prediction=f'Error: {e}')

# #     return render_template('index.html', prediction=None)

# # if __name__ == '__main__':
# #     app.run(debug=True)

# from flask import Flask, render_template, request
# import pandas as pd
# import pickle
# from scripts.data_preprocessing import preprocess_input

# app = Flask(__name__)

# # Load the models
# with open('models/trained_model_home.pkl', 'rb') as f:
#     model_home = pickle.load(f)

# with open('models/trained_model_away.pkl', 'rb') as f:
#     model_away = pickle.load(f)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     prediction = None
#     if request.method == 'POST':
#         home_team = request.form.get('home_team')
#         away_team = request.form.get('away_team')

#         if not home_team or not away_team:
#             return render_template('index.html', prediction='Invalid input. Please provide both home and away teams.')

#         try:
#             input_data = preprocess_input(home_team, away_team)

#             # Make predictions
#             home_goals_pred = model_home.predict(input_data)[0]
#             away_goals_pred = model_away.predict(input_data)[0]

#             return render_template('index.html', prediction=(home_goals_pred, away_goals_pred))
#         except ValueError as e:
#             return render_template('index.html', prediction=f'Error: {e}')

#     return render_template('index.html', prediction=None)

# if __name__ == '__main__':
#     app.run(debug=True)


from flask import Flask, render_template, request
import pandas as pd
import pickle
from scripts.data_preprocessing import preprocess_input

app = Flask(__name__)

# Load the models
with open('models/trained_model_home.pkl', 'rb') as f:
    model_home = pickle.load(f)

with open('models/trained_model_away.pkl', 'rb') as f:
    model_away = pickle.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    if request.method == 'POST':
        home_team = request.form.get('home_team')
        away_team = request.form.get('away_team')

        if not home_team or not away_team:
            return render_template('index.html', prediction='Invalid input. Please provide both home and away teams.')

        try:
            input_data = preprocess_input(home_team, away_team)

            # Make predictions
            home_goals_pred = model_home.predict(input_data)[0]
            away_goals_pred = model_away.predict(input_data)[0]

            # Round predictions to the nearest whole number
            home_goals_pred = round(home_goals_pred)
            away_goals_pred = round(away_goals_pred)

            return render_template('index.html', prediction=(home_goals_pred, away_goals_pred))
        except ValueError as e:
            return render_template('index.html', prediction=f'Error: {e}')

    return render_template('index.html', prediction=None)

if __name__ == '__main__':
    app.run(debug=True)
