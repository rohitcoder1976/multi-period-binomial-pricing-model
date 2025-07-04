def compute_all_call_payoffs(n: int, stock_prices: list[list[float]], K: float):
    all_call_payoffs = []
    for r_i in range(n + 1):
        i = n - r_i
        call_payoffs = []
        for j in range(i + 1):
            call_payoffs.append(max(stock_prices[i][j] - K, 0))
        all_call_payoffs.append(call_payoffs)
    return all_call_payoffs

def compute_all_call_prices(n: int, all_call_payoffs: list[list[float]], q: float):
    all_call_prices = []
    for r_i in range(n + 1):
        i = n - r_i
        call_prices = []
        if i == n: # if at the last step, the prices are the payoffs (arbitrage-free pricing)
            call_prices.append(all_call_payoffs[i])
        else:
            for j in range(i + 1):
                price = (q * all_call_prices[i + 1][j + 1]) + (1-q) * all_call_prices[i + 1][j]
                call_prices.append(price)
        all_call_prices.append(call_prices)
    return all_call_prices