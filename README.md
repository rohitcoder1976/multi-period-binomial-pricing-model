## Introduction

This is a simple computation tool used to compute stock prices and arbitrage-free (or fair-value) prices of futures and options contracts in a multi-period binomial model, using predefined parameters (such as risk-free interest rate `r` and dividend yield of underlying stock `c`) at the top of the `main.py` file.

This project does not use any sophisticated libraries such as NumPy for computation, and is meant for basic use cases that may prove helpful in academic settings.

This project also uses more of a continuous Black-Scholes method in calculating prices (as evidenced by the computations of discounts and up-and-down factors `u` and `d`) rather than a strcictly discrete binomial method.

## Getting Started

- Since this project does not use any external python libraries, a virtual environment is not needed.
- Clone the repository
- Make sure you have python installed by running one of the following:

```
    python --version
```

```
    python3 --version
```

- While in the root directory of the project, run the project using one of the following:

```
    python main.py
```

```
    python3 main.py
```

## Calibration

You can change the parameters of the project (such as initial stock price `s0` and risk-free rate `r`) at the top of the `main.py` file.

You can use the `print_prices` method imported in the `main.py` file to print out any of the prices you desire.
