def compute_all_call_payoffs(n: int, stock_prices: list[list[float]], K: float):
    all_call_payoffs = []
    for i in range(n + 1):
        call_payoffs = []
        for j in range(i + 1):
            call_payoffs.append(max(stock_prices[i][j] - K, 0))
        all_call_payoffs.append(call_payoffs)
    return all_call_payoffs

def compute_all_put_payoffs(n: int, stock_prices: list[list[float]], K: float):
    all_put_payoffs = []
    for i in range(n + 1):
        put_payoffs = []
        for j in range(i + 1):
            put_payoffs.append(max(K - stock_prices[i][j], 0))
        all_put_payoffs.append(put_payoffs)
    return all_put_payoffs

def compute_all_call_prices(n: int, all_call_payoffs: list[list[float]], q: float):
    all_call_prices = [[]] * (n+1) 
    for r_i in range(n + 1):
        i = n - r_i
        if i == n: # if at the last step, the prices are the payoffs (arbitrage-free pricing)
            all_call_prices[i] = all_call_payoffs[i]
        else:
            call_prices = []
            for j in range(i + 1):
                price = (q * all_call_prices[i + 1][j + 1]) + (1-q) * all_call_prices[i + 1][j]
                call_prices.append(price)
            all_call_prices[i] = call_prices
    return all_call_prices

def compute_all_european_put_prices(n: int, all_put_payoffs: list[list[float]], q: float):
    all_put_prices = [[]] * (n+1) 
    for r_i in range(n + 1):
        i = n - r_i
        if i == n: # if at the last step, the prices are the payoffs (arbitrage-free pricing)
            all_put_prices[i] = all_put_payoffs[i]
        else:
            put_prices = []
            for j in range(i + 1):
                price = (q * all_put_prices[i + 1][j + 1]) + (1-q) * all_put_prices[i + 1][j]
                put_prices.append(price)
            all_put_prices[i] = put_prices
    return all_put_prices

def compute_all_american_put_prices(n: int, all_put_payoffs: list[list[float]], q: float):
    all_put_prices = [[]] * (n+1)
    for r_i in range(n + 1):
        i = n - r_i
        if i == n: # if at the last step, the prices are the payoffs (arbitrage-free pricing)
            all_put_prices[i] = all_put_payoffs[i]
        else:
            put_prices = []
            for j in range(i + 1):
                price = (q * all_put_prices[i + 1][j + 1]) + (1-q) * all_put_prices[i + 1][j]
                put_prices.append(max(price, all_put_payoffs[i][j]))
            all_put_prices[i] = put_prices
    return all_put_prices