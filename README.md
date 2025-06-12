# Message Spam Detection Project

This project builds a machine learning model to classify SMS messages as **spam** or **ham** (not spam).

## Project Structure

- `data/spam.csv` : Place your SMS Spam Collection dataset here.
- `src/data_preprocessing.py` : Functions for cleaning and preprocessing text data.
- `src/model.py` : Script for training and evaluating the model.
- `src/predict.py` : Script for loading the trained model and predicting new messages.
- `run.py` : Main script to run training and evaluation.
- `requirements.txt` : Python dependencies.

## How to Run

1. Place `spam.csv` dataset in the `data/` folder.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the main script: `python run.py`

