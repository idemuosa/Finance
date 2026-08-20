from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Dict
import pandas as pd
import numpy as np

# Import models
from src.models.fraud_detection import FraudDetector
from src.models.credit_risk import CreditRiskModel
from src.models.customer_scoring import CustomerRiskScorer
from src.models.anomaly_detection import TransactionAnomalyDetector

app = FastAPI(title="Finance Data Science API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the actual frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize models
fraud_detector = FraudDetector()
credit_model = CreditRiskModel()
risk_scorer = CustomerRiskScorer()
anomaly_detector = TransactionAnomalyDetector()

class Transaction(BaseModel):
    amount: float
    merchant_id: int
    user_id: int

@app.get("/")
async def root():
    return {"message": "Welcome to the Finance Data Science API"}

@app.post("/predict/fraud")
async def predict_fraud(data: List[Dict]):
    # Implementation placeholder
    return {"message": "Fraud prediction endpoint"}

@app.post("/predict/credit-risk")
async def predict_credit_risk(data: List[Dict]):
    return {"message": "Credit risk prediction endpoint"}

@app.post("/score/customer")
async def score_customer(data: Dict):
    df = pd.DataFrame([data])
    score = risk_scorer.calculate_score(df)
    tier = risk_scorer.get_risk_tier(score)
    return {"score": score, "risk_tier": tier}

@app.get("/health")
async def health():
    return {"status": "healthy"}
