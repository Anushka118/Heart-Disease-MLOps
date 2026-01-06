#!/bin/bash
set -e

echo "Starting Production Readiness Verification..."

# 1. Verification of Clean Environment Setup
echo "Step 1: Verifying dependency installation from requirements.txt..."
python3 -m venv venv_prod
source venv_prod/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "Dependencies installed successfully."

# 2. Verification of Test Execution
echo "Step 2: Running Unit Tests..."
export PYTHONPATH=$PYTHONPATH:.
pytest test/
echo "Tests passed successfully."

# 3. Verification of Model Serving Artifacts
echo "Step 3: Checking model artifacts..."
if [ -f "heart_disease_pipeline.pkl" ]; then
    echo "Model artifact found."
else
    echo "ERROR: Model artifact 'heart_disease_pipeline.pkl' not found!"
    exit 1
fi

echo "Production Readiness Verification Completed Successfully."
# Cleanup
deactivate
rm -rf venv_prod
