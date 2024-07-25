import subprocess

def run_pipeline():
    # Run data preprocessing
    subprocess.run(['python', 'scripts/data_preprocessing.py'])

    # Run feature engineering
    subprocess.run(['python', 'scripts/feature_engineering.py'])

    # Train the model
    subprocess.run(['python', 'scripts/model_training.py'])

    # Evaluate the model
    subprocess.run(['python', 'scripts/model_evaluation.py'])

if __name__ == "__main__":
    run_pipeline()
