def compute_all_stock_prices(n: int, s0: float, u: float, d: float):
    all_prices = []
    for i in range(n + 1):
        if i == 0:
            prices = [s0]
        else:
            prices = []
            for j in range(i + 1):
                prices.append(s0 * (u ** j) * (d ** (i - j)))
        all_prices.append(prices)
    return all_prices