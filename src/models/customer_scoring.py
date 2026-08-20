import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

class CustomerRiskScorer:
    def __init__(self):
        self.scaler = MinMaxScaler()

    def calculate_score(self, df):
        """
        Calculates a risk score based on weighted financial indicators.
        Expected columns: debt_to_income, payment_history, utilization_ratio
        """
        features = ['debt_to_income', 'payment_history', 'utilization_ratio']

        # Simple weighted sum model
        weights = {
            'debt_to_income': 0.4,
            'payment_history': 0.4,
            'utilization_ratio': 0.2
        }

        score = sum(df[feature] * weights[feature] for feature in features)
        return score

    def get_risk_tier(self, score):
        if score < 0.3: return "Low"
        if score < 0.7: return "Medium"
        return "High"
