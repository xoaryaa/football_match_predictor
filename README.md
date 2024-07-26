# Football Match Predictor

This project predicts the number of goals for the home and away teams in football matches using machine learning. The application is built with Python and Flask, and uses scikit-learn for the model training.

## Table of Contents
- [Football Match Predictor](#football-match-predictor)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Data](#data)
  - [Model Training](#model-training)

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/football-match-predictor.git
    cd football-match-predictor
    ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Prepare the dataset:**
   - Ensure you have the dataset file `match_data.csv` in the `data` directory.
   - The CSV file should have the following columns: `Season_End_Year`, `Wk`, `Date`, `HomeTeam`, `HomeGoals`, `AwayTeam`, `AwayGoals`, `FTR`.

2. **Train the models:**
    ```bash
    python model_training.py
    ```

3. **Run the Flask application:**
    ```bash
    python app.py
    ```

4. **Access the web interface:**
    - Open your web browser and go to `http://127.0.0.1:5000/`.

## Data

The `match_data.csv` file should be placed in the `data` directory. It should contain the following columns:

- `Season_End_Year`: The season end year.
- `Wk`: The week of the match.
- `Date`: The date of the match.
- `HomeTeam`: The name of the home team.
- `HomeGoals`: The number of goals scored by the home team.
- `AwayTeam`: The name of the away team.
- `AwayGoals`: The number of goals scored by the away team.
- `FTR`: The full-time result of the match.

## Model Training

The `model_training.py` script handles model training. It loads the data, encodes the team names, trains two separate models for predicting home and away goals, and saves the trained models and label encoder.

```python

