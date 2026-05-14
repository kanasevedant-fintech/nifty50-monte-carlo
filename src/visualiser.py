import matplotlib.pyplot as plt
import numpy as np

# Chart 1 — fan of simulated price paths over 5 days
def plot_simulation_paths(price_paths, save_path=None):
    n_days, n_simulations = price_paths.shape
    days = np.arange(n_days)
    sample_paths = price_paths[:, :200]

    plt.figure(figsize=(10, 6))
    for i in range(sample_paths.shape[1]):
        plt.plot(days, sample_paths[:, i], color='blue', alpha=0.05)
    mean_path = np.mean(price_paths, axis=1)
    plt.plot(days, mean_path, color='red', linewidth=2, label='Mean Path')
    plt.axhline(y=price_paths[0, 0], color='gray', linestyle='--', label="Today's Price")
    plt.xlabel('Trading Days Forward')
    plt.ylabel('Nifty 50 Price')
    plt.title('Monte Carlo Simulation — Nifty 50 (Next 5 Days)')
    plt.legend()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()

# Chart 2 — histogram of all simulated prices on day 5 with percentile markers
def plot_final_distribution(price_paths, save_path=None):
    final_prices = price_paths[-1]
    left_tail = np.percentile(final_prices, 5)
    median = np.percentile(final_prices, 50)
    right_tail = np.percentile(final_prices, 95)

    plt.figure(figsize=(10, 6))
    plt.hist(final_prices, bins=50, color='blue', alpha=0.7)
    plt.axvline(left_tail, color='red', linestyle='--', label=f'5th pct: {left_tail:.2f}')
    plt.axvline(median, color='green', linestyle='--', label=f'Median: {median:.2f}')
    plt.axvline(right_tail, color='orange', linestyle='--', label=f'95th pct: {right_tail:.2f}')
    plt.xlabel('Simulated Price on Day 5')
    plt.ylabel('Frequency')
    plt.title('Distribution of Simulated Prices on Day 5')
    plt.legend()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()

# Chart 3 — cone of uncertainty showing 5th-95th percentile band across all 5 days
def plot_confidence_band(price_paths, save_path=None):
    n_days, n_simulations = price_paths.shape
    days = np.arange(n_days)
    lower_band = np.percentile(price_paths, 5, axis=1)
    upper_band = np.percentile(price_paths, 95, axis=1)
    mean_path = np.mean(price_paths, axis=1)

    plt.figure(figsize=(10, 6))
    plt.fill_between(days, lower_band, upper_band, color='blue', alpha=0.3, label='5th-95th Percentile Band')
    plt.plot(days, mean_path, color='red', linewidth=2, label='Mean Path')
    plt.axhline(y=price_paths[0, 0], color='gray', linestyle='--', label="Today's Price")
    plt.xlabel('Trading Days Forward')
    plt.ylabel('Nifty 50 Price')
    plt.title('Monte Carlo Simulation — Confidence Band (Next 5 Days)')
    plt.legend()
    if save_path:
        plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.show()
