import pandas as pd
from prophet import Prophet

class FinancialForecaster:
    def __init__(self):
        self.model = None

    def forecast(self, df, periods=30):
        """
        Uses Facebook Prophet for time series forecasting.
        df must have 'ds' (date) and 'y' (value) columns.
        """
        self.model = Prophet(daily_seasonality=True)
        self.model.fit(df)

        future = self.model.make_future_dataframe(periods=periods)
        forecast = self.model.predict(future)
        return forecast
