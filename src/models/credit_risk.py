import pandas as pd
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

class CreditRiskModel:
    def __init__(self):
        self.model = None

    def train(self, X, y):
        # Using LightGBM for credit risk as it handles categorical features well
        self.model = lgb.LGBMClassifier(
            objective='binary',
            metric='auc',
            boosting_type='gbdt',
            num_leaves=31,
            learning_rate=0.05,
            feature_fraction=0.9
        )
        self.model.fit(X, y)

    def predict_proba(self, X):
        if self.model is None:
            raise ValueError("Model not trained")
        return self.model.predict_proba(X)
