import config
from src import data_fetcher, returns_calculator, monte_carlo, visualiser

df = data_fetcher.download_data(
    ticker=config.TICKER,
    start=config.START_DATE,
    end=config.END_DATE,
    interval=config.INTERVAL,
    save_path=f"{config.RAW_DATA_PATH}{config.TICKER}.csv"
)

log_returns = returns_calculator.compute_log_returns(df["Close"])
mu, sigma = returns_calculator.compute_drift_and_volatility(log_returns)
print(f"Daily drift (mu):         {mu:.6f}")
print(f"Daily volatility (sigma): {sigma:.6f}")

last_price = df["Close"].iloc[-1]
print(f"Last closing price:       {last_price:,.2f}")

price_paths = monte_carlo.run_simulation(
    last_price=last_price,
    mu=mu,
    sigma=sigma,
    n_days=config.N_DAYS,
    n_simulations=config.N_SIMULATIONS
)

summary = monte_carlo.summarise_results(price_paths)
print(f"5th  percentile:          {summary['percentile_5']:.0f}")
print(f"95th percentile:          {summary['percentile_95']:.0f}")
print(f"Expected Price (mean):    {summary['mean_price']:.0f}")

print("\nDay-by-day mean forecast:")
for day in range(1, config.N_DAYS + 1):
    day_mean = float(price_paths[day].mean())
    print(f"  Day {day}: {day_mean:,.2f}")

visualiser.plot_simulation_paths(
    price_paths=price_paths,
    save_path=f"{config.PLOTS_PATH}simulation_paths.png"
)
visualiser.plot_final_distribution(
    price_paths=price_paths,
    save_path=f"{config.PLOTS_PATH}final_distribution.png"
)
visualiser.plot_confidence_band(
    price_paths=price_paths,
    save_path=f"{config.PLOTS_PATH}confidence_band.png"
)
