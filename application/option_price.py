from scipy.stats import norm
import numpy as np

# Define the Black-Scholes Equation for a European Call Option
def f(sigma):
    """
    S: spot price
    K: strike price
    T: time to maturity
    r: risk-free interest rate
    q: dividend yield
    sigma: volatility
    """
    S = 30
    K = 30
    T = 0.5
    r = 0.03
    q = 0.01
    C_m = 2.5
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2) - C_m

# Derivative of the Black-Scholes Equation with respect to sigma (vega)
def df(sigma):
    S = 30
    K = 30
    T = 0.5
    r = 0.03
    q = 0.01
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return S * np.sqrt(T) * np.exp(-q * T) * norm.pdf(d1)

C_m = 2.5 # Market price of the call option

try:
    implied_vol = newton_method(f, df, 0.5, 1e-6)
    print(f"The implied volatility is: {implied_vol}")
except ValueError as e:
    print(e)
