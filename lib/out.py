def print_prices(all_prices: list[list[float]]):
    for i in all_prices:
        for j in i:
            print(f"{j:.4f}", end=" ")
        print()