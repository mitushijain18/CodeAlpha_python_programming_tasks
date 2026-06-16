# Hardcoded dictionary of stock prices
stock_prices = {
    "AAPL": 150,
    "TSLA": 200,
    "GOOGL": 2800,
    "AMZN": 3300
}

def calculate_portfolio():
    print("--- Stock Portfolio Tracker ---")
    total_value = 0
    
    while True:
        symbol = input("Enter stock symbol (or 'done' to finish): ").upper()
        if symbol == 'DONE':
            break
            
        if symbol in stock_prices:
            try:
                quantity = int(input(f"How many shares of {symbol} do you own? "))
                value = stock_prices[symbol] * quantity
                total_value += value
                print(f"Added {symbol}: ${value}")
            except ValueError:
                print("Please enter a valid number for quantity.")
        else:
            print("Stock symbol not found in database.")

    print(f"\nYour total portfolio value is: ${total_value}")

if __name__ == "__main__":
    calculate_portfolio()