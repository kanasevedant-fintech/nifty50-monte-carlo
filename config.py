import datetime

TICKER = "^NSEI"
START_DATE = "2020-01-01"
END_DATE = datetime.datetime.today().strftime("%Y-%m-%d")
INTERVAL = "1d"

N_SIMULATIONS = 1000
N_DAYS = 5
TRADING_DAYS_PER_YEAR = 252

RAW_DATA_PATH = "data/raw/"
PLOTS_PATH = "outputs/plots/"
