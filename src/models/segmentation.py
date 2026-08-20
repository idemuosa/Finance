import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class CustomerSegmenter:
    def __init__(self, n_clusters=5):
        self.n_clusters = n_clusters
        self.scaler = StandardScaler()
        self.model = KMeans(n_clusters=n_clusters, random_state=42)

    def segment(self, X):
        """
        Segments customers based on behavior features.
        """
        X_scaled = self.scaler.fit_transform(X)
        clusters = self.model.fit_predict(X_scaled)
        return clusters
