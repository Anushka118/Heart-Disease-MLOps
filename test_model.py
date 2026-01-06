import pandas as pd
import joblib
import os
import pytest
from sklearn.pipeline import Pipeline

# Define paths
MODEL_PATH = 'heart_disease_pipeline.pkl'
DATA_PATH = 'heart_disease_cleaned.csv'

def test_files_exist():
    """Test 1: Check if model and data files exist"""
    assert os.path.exists(DATA_PATH), "Cleaned dataset not found"
    assert os.path.exists(MODEL_PATH), "Model file not found"

def test_model_loading():
    """Test 2: Check if the model pipeline loads successfully"""
    model = joblib.load(MODEL_PATH)
    assert isinstance(model, Pipeline), "Loaded object is not a pipeline"

def test_prediction_shape():
    """Test 3: Ensure model predicts correctly using a sample from the dataset"""
    # Load the model
    model = joblib.load(MODEL_PATH)
    
    # Load the actual dataset to get the correct column structure
    df = pd.read_csv(DATA_PATH)
    
    # Drop the target column to simulate input data
    # (Task 1 saved the target as 'target')
    if 'target' in df.columns:
        X_sample = df.drop(columns=['target']).iloc[[0]] # Get the first row
    else:
        # Fallback if target column has a different name
        X_sample = df.iloc[[0, :-1]] 

    # Predict
    prediction = model.predict(X_sample)
    
    # Assertions
    assert len(prediction) == 1, "Model did not return a prediction"
    assert prediction[0] in [0, 1], f"Invalid prediction value: {prediction[0]}"

if __name__ == "__main__":
    pytest.main()