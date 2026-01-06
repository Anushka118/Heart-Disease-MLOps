import pandas as pd
import numpy as np
import joblib
import os
import pytest
from sklearn.pipeline import Pipeline

# Define paths
MODEL_PATH = 'heart_disease_pipeline.pkl'
DATA_PATH = 'heart_disease_cleaned.csv' # Assuming you saved this in Task 1

def test_dataset_exists():
    """Test 1: Check if the cleaned dataset file exists"""
    assert os.path.exists(DATA_PATH), f"Dataset not found at {DATA_PATH}"

def test_model_loading():
    """Test 2: Check if the model pipeline loads successfully"""
    assert os.path.exists(MODEL_PATH), "Model file not found"
    model = joblib.load(MODEL_PATH)
    assert isinstance(model, Pipeline), "Loaded object is not a scikit-learn Pipeline"

def test_prediction_shape():
    """Test 3: Ensure model accepts input and returns binary prediction"""
    model = joblib.load(MODEL_PATH)
    
    # Create a dummy input with the same structure as training data
    # (Adjust feature names to match your X_train columns exactly)
    # This example assumes the standard 13-14 features
    dummy_data = pd.DataFrame([{
        'age': 63, 'sex': 1, 'cp': 3, 'trestbps': 145, 'chol': 233, 
        'fbs': 1, 'restecg': 0, 'thalach': 150, 'exang': 0, 
        'oldpeak': 2.3, 'slope': 0, 'ca': 0, 'thal': 1
    }])
    
    # Ensure columns match what the scaler expects. 
    # If you get a 'feature mismatch' error, align these cols with X_train.columns
    
    prediction = model.predict(dummy_data)
    assert len(prediction) == 1, "Model did not return a single prediction"
    assert prediction[0] in [0, 1], "Prediction is not binary (0 or 1)"

if __name__ == "__main__":
    # Allow running directly for manual testing
    pytest.main()