import pandas as pd
import joblib
from flask import Flask, request, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import logging
import sys

# Configure logging
logging.basicConfig(
    stream=sys.stdout,
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger('heart-disease-api')

app = Flask(__name__)
# Initialize Prometheus metrics
metrics = PrometheusMetrics(app)

# Load the model
model_path = 'heart_disease_pipeline.pkl'
try:
    model = joblib.load(model_path)
    logger.info("Model loaded successfully")
except Exception as e:
    logger.error(f"Error loading model: {e}")
    model = None

@app.route('/predict', methods=['POST'])
@metrics.counter('prediction_requests', 'Number of prediction requests')
def predict():
    if not model:
        logger.error("Predict called but model is not loaded")
        return jsonify({'error': 'Model not loaded'}), 500

    try:
        data = request.get_json()
        logger.info(f"Received prediction request: {data}")
        
        # Convert input dictionary to DataFrame
        # Expecting input to match the features used in training
        input_data = pd.DataFrame([data])
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Try to get prediction probability if available
        if hasattr(model, 'predict_proba'):
            confidence = model.predict_proba(input_data).max()
        else:
            confidence = None
            
        result = {
            'prediction': int(prediction[0]),
            'confidence': float(confidence) if confidence is not None else "N/A"
        }
        
        logger.info(f"Prediction result: {result}")
        return jsonify(result)

    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
