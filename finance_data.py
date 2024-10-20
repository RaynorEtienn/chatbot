import yfinance as yf

def get_forex_data(symbol):
	"""Function used to get the current price of a Forex pair.

	Args:
		symbol (str): Wanted Forex pair.

	Returns:
		current_price (np.f64): Float value of the wanted pair.
	"""
	# Create a ticker object for the Forex pair
	ticker = yf.Ticker(f"{symbol}=X")

	# Fetch current price and historical data
	forex_info = ticker.history(period="1d")

	# Get the latest close price
	current_price = forex_info['Close'].iloc[-1]

	return current_price

if __name__ == "__main__":
	print(get_forex_data("EURUSD"))
