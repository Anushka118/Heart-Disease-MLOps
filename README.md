# Heart Disease MLOps Pipeline

This repository contains an end-to-end MLOps solution for heart disease classification. It includes data processing, model training, automated testing, containerization, and Kubernetes deployment instructions.

## Quick Start

### 1. Installation
```bash
pip install -r requirements.txt
```

### 2. Run Locally
To start the model serving API:
```bash
python app.py
```

### 3. Docker Build & Run
```bash
docker build -t heart-disease-api .
docker run -p 5000:5000 heart-disease-api
```

### 4. Full Documentation
Please refer to [REPORT.md](REPORT.md) for detailed documentation on:
*   Project Architecture
*   EDA & Modeling Decisions
*   CI/CD Pipelines
*   Kubernetes Deployment
*   Monitoring Setup
