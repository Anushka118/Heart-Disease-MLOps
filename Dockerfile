FROM python:3.9-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code and model
COPY app.py .
COPY heart_disease_pipeline.pkl .

# Expose port
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
