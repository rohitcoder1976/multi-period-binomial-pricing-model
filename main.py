import math
from compute_stock import compute_all_stock_prices
from compute_options import compute_all_call_payoffs, compute_all_call_prices

T = 0.25
s0 = 100
K = 110
sigma = 0.3
r = 0.02
c = 0.01
n = 15

def compute_u_and_d():
    u = math.exp(sigma * math.sqrt(T / n))
    d = 1 / u
    return u, d

u, d = compute_u_and_d()
q = (math.exp((r - c) * T / n) - d) / (u - d)

stock_prices = compute_all_stock_prices(s0=s0, u=u, d=d, n=n)
all_call_payoffs = compute_all_call_payoffs(K=K, n=n, stock_prices=stock_prices)
all_call_prices = compute_all_call_prices(q=q, n=n, all_call_payoffs=all_call_payoffs)
for i in all_call_prices:
    for j in i:
        print(f"{j:.2f}", end=" ")
    print()