# Finance Data Science Project

## Overview
This project focuses on various financial data science challenges using a robust stack of tools and frameworks.

## Main Problems
- **Fraud detection**: Identifying fraudulent transactions and activities.
- **Credit/loan risk**: Assessing the likelihood of a borrower defaulting.
- **Customer risk scoring**: Evaluating individual customer profiles for risk.
- **Financial forecasting**: Predicting future financial trends and values.
- **Portfolio/risk analysis**: Analyzing investment portfolios and associated risks.
- **Transaction anomaly detection**: Spotting unusual patterns in financial transactions.
- **Customer segmentation**: Categorizing customers based on behavior and characteristics.

## Frameworks & Tools
- **Languages & Databases**: Python, various databases.
- **Data Manipulation**: pandas, numpy, scipy.
- **Statistical Modeling**: statsmodels, prophet.
- **Machine Learning**: scikit-learn, XGBoost, LightGBM.
- **Visualization**: matplotlib, seaborn, plotly, Plotly Dash.
- **Financial Data**: yfinance, pandas-datareader.
- **Backend & APIs**: FastAPI, Django + Django REST Framework (DRF).
- **Asynchronous Processing**: Celery, Redis.
- **Deep Learning**: PyTorch.
- **MLOps**: MLflow.
- **Deployment**: Docker, AWS.

## Project Structure
- `src/models/`: Contains the core machine learning and statistical models.
    - [fraud_detection.py](file:///C:/Users/bonmm/OneDrive/Desktop/finance/src/models/fraud_detection.py): XGBoost-based fraud detection.
    - [credit_risk.py](file:///C:/Users/bonmm/OneDrive/Desktop/finance/src/models/credit_risk.py): LightGBM model for loan default prediction.
    - [customer_scoring.py](file:///C:/Users/bonmm/OneDrive/Desktop/finance/src/models/customer_scoring.py): Risk scoring logic for customer profiles.
    - [forecasting.py](file:///C:/Users/bonmm/OneDrive/Desktop/finance/src/models/forecasting.py): Time-series forecasting using Prophet.
    - [portfolio_analysis.py](file:///C:/Users/bonmm/OneDrive/Desktop/finance/src/models/portfolio_analysis.py): Financial analysis tools (Sharpe, VaR).
    - [anomaly_detection.py](file:///C:/Users/bonmm/OneDrive/Desktop/finance/src/models/anomaly_detection.py): Isolation Forest for transaction anomalies.
    - [segmentation.py](file:///C:/Users/bonmm/OneDrive/Desktop/finance/src/models/segmentation.py): K-Means clustering for customer segmentation.
- `src/api/`: FastAPI implementation for exposing models as services.
- `src/tasks/`: Celery task definitions for asynchronous processing.
### Installation
To install the required dependencies, run:
```bash
pip install -r requirements.txt
```
