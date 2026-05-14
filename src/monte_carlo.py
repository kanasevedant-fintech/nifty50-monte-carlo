import numpy as np

# Simulates N price paths using Geometric Brownian Motion (GBM)
def run_simulation(last_price, mu, sigma, n_days, n_simulations):
    price_paths = np.zeros((n_days + 1, n_simulations))
    price_paths[0] = last_price
    random_shocks = np.random.standard_normal((n_days, n_simulations))
    for day in range(1, n_days + 1):
        daily_return = np.exp((mu - 0.5 * sigma**2) + sigma * random_shocks[day - 1])
        price_paths[day] = price_paths[day - 1] * daily_return
    return price_paths

# Returns summary statistics for the final simulated day
def summarise_results(price_paths):
    final_prices = price_paths[-1]
    summary = {
        "mean_price": np.mean(final_prices),
        "median_price": np.median(final_prices),
        "percentile_5": np.percentile(final_prices, 5),
        "percentile_95": np.percentile(final_prices, 95),
        "std_dev": np.std(final_prices)
    }
    return summary
