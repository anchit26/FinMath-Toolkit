from sympy import symbols, exp, sqrt, log, Function, diff
from sympy.stats import Normal, cdf
from sympy.utilities.lambdify import lambdify
from sympy import solve
from scipy.stats import norm
import math

# Define the symbols
S0, K, r, sigma = 45, 45, 0.02, 0.25

# Black-Scholes formula for put option
def d1(t):
  return (math.log(S0 / K) + (r + sigma**2 / 2) * t) / (sigma * math.sqrt(t))

def d2(t):
  return d1(t) - sigma * math.sqrt(t)

def delta(x, y, z):
  return (x - y)/2/z

def gamma(w, x, y, z):
  return (x - 2 * w + y)/z/z

w = 2.47
x = 2.47
y = 2.47
z = 0.001
delta(x, y, z), gamma(w, x, y, z)

def V(time):
  global S0, K, r,sigma
  return K * math.exp(-r * time) * norm.cdf(-1 * d2(time)) - S0  * norm.cdf(-1 * d1(time))

def theta(T, dt):
  return (V(T - dt) - V(T))/dt

haha = 0.5
dt = 1/8/252

theta(haha, dt)