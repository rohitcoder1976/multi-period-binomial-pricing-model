def compute_futures_prices(n: int, stock_prices: list[list[float]], q: float):
    all_futures_prices = [[]] * (n + 1)
    for r_i in range(n + 1):
        i = n - r_i
        # if at the last step, the futures price equals the stock price to make the value of the contract equal to 0
        if i == n: 
            all_futures_prices[i] = stock_prices[i]
        else:
            futures_prices = []
            for j in range(i + 1):
                price = (q * all_futures_prices[i + 1][j + 1]) + (1-q) * all_futures_prices[i + 1][j]
                futures_prices.append(price)
            all_futures_prices[i] = futures_prices
    return all_futures_prices