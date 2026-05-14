# Nifty 50 Monte Carlo Price Simulation

A Monte Carlo simulation engine that forecasts the next 5 trading days of the Nifty 50 index using Geometric Brownian Motion (GBM). Built from scratch in Python as part of my quantitative finance learning journey.

---

## What It Does

- Downloads historical daily Nifty 50 data via `yfinance`
- Computes daily log returns, drift (μ), and volatility (σ) from historical data
- Simulates 1000 independent price paths over the next 5 trading days using GBM
- Outputs a statistical forecast range (5th percentile, median, 95th percentile)
- Generates 3 charts: simulation fan, price distribution, and confidence band

---

## The Math

Each simulated price step follows the **Geometric Brownian Motion** formula:

```
S(t+1) = S(t) × exp( (μ - 0.5σ²) + σ × Z )
```

Where:
- `μ` = mean daily log return (drift)
- `σ` = standard deviation of daily log returns (volatility)
- `Z` = random draw from Standard Normal distribution N(0,1)
- `0.5σ²` = Ito correction to prevent upward bias in simulated paths

---

## Project Structure

```
nifty50-monte-carlo/
├── config.py                  # all constants: ticker, dates, simulation params
├── main.py                    # entry point — runs the full pipeline
├── requirements.txt
├── src/
│   ├── data_fetcher.py        # downloads and caches Nifty 50 data via yfinance
│   ├── returns_calculator.py  # computes log returns, drift, and volatility
│   ├── monte_carlo.py         # GBM simulation engine + summary statistics
│   └── visualiser.py          # generates 3 matplotlib charts
├── data/raw/                  # downloaded CSV cached here
└── outputs/plots/             # saved chart PNGs
```

---

## Setup & Run

**1. Clone the repository**
```bash
git clone https://github.com/your-username/nifty50-monte-carlo.git
cd nifty50-monte-carlo
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run**
```bash
python main.py
```

---

## Sample Terminal Output

```
Downloading data for ^NSEI from 2020-01-01 to 2026-05-15...
Daily drift (mu):         0.000412
Daily volatility (sigma): 0.009813
Last closing price:       24,315.00

5th  percentile:          23,891
95th percentile:          24,762
Expected Price (mean):    24,321

Day-by-day mean forecast:
  Day 1: 24,318.45
  Day 2: 24,321.87
  Day 3: 24,325.12
  Day 4: 24,328.34
  Day 5: 24,331.56
```

---

## Charts Generated

| Chart | Description |
|---|---|
| Simulation Paths | Fan of 200 sampled price paths with mean path overlay |
| Final Distribution | Histogram of all simulated Day 5 prices with percentile markers |
| Confidence Band | Cone of uncertainty — 5th to 95th percentile band across all 5 days |

---

## Planned Enhancements

- [ ] Value at Risk (VaR) and Conditional VaR (CVaR)
- [ ] Backtesting against actual price outcomes
- [ ] Rolling volatility analysis
- [ ] GARCH volatility modelling
- [ ] Multi-asset portfolio simulation
