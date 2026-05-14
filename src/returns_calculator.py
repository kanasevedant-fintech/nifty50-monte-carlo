import numpy as np

def compute_log_returns(close_series):
    log_returns = np.log(close_series / close_series.shift(1))
    log_returns.dropna(inplace=True)
    return log_returns

def compute_drift_and_volatility(log_returns):
    mu = float(log_returns.mean())
    sigma = float(log_returns.std())
    return mu, sigma
