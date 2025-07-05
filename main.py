import math
from compute.stock import compute_all_stock_prices
from compute.options import compute_all_call_payoffs, compute_all_european_call_prices, compute_all_american_call_prices, compute_all_american_put_prices, compute_all_european_put_prices, compute_all_put_payoffs
from compute.futures import compute_futures_prices
from lib.out import print_prices

T = 0.25 # the total time of all periods combined, in years
s0 = 100 # initial stock price
K = 110 # strike price for options
sigma = 0.3 # volatility of underlying stock
r = 0.02 # risk-free rate
c = 0.01 # dividend yield of underlying stock
n = 15 # number of periods

def compute_u_and_d():
    u = math.exp(sigma * math.sqrt(T / n))
    d = 1 / u
    return u, d

u, d = compute_u_and_d()
q = (math.exp((r - c) * T / n) - d) / (u - d)

stock_prices = compute_all_stock_prices(s0=s0, u=u, d=d, n=n)

all_call_payoffs = compute_all_call_payoffs(K=K, n=n, prices=stock_prices)
all_call_prices = compute_all_european_call_prices(
    q=q, 
    n=n, 
    all_call_payoffs=all_call_payoffs, 
    r=r, 
    T=T, 
    discounting=True
)

all_put_payoffs = compute_all_put_payoffs(K=K, n=n, prices=stock_prices)
all_european_put_prices = compute_all_european_put_prices(q=q, n=n, all_put_payoffs=all_put_payoffs, r=r, T=T)
all_american_put_prices = compute_all_american_put_prices(q=q, n=n, all_put_payoffs=all_put_payoffs, r=r, T=T)

all_futures_prices = compute_futures_prices(n=n, stock_prices=stock_prices, q=q)
all_call_prices_on_futures = compute_all_american_call_prices(
    n=10, 
    all_call_payoffs=compute_all_call_payoffs(n=10, prices=all_futures_prices, K=K), 
    q=q, 
    T=T, 
    r=r, 
    discounting=False
)

print_prices(all_call_prices_on_futures)