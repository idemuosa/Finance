import pandas as pd
from sklearn.ensemble import IsolationForest

class TransactionAnomalyDetector:
    def __init__(self, contamination=0.01):
        self.model = IsolationForest(contamination=contamination, random_state=42)

    def detect(self, X):
        """
        Returns -1 for anomalies and 1 for normal transactions.
        """
        self.model.fit(X)
        return self.model.predict(X)

    def get_anomaly_scores(self, X):
        return self.model.decision_function(X)
