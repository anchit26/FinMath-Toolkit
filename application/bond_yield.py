import math


def bond_value(y):
  global coupon, face_val, cash_flows, yearly_frequency
  bond_val = 0
  for i in range (1, cash_flows):
    bond_val = bond_val + coupon * math.exp(-y * i/yearly_frequency)

  # maturity
  bond_val = bond_val + (face_val + coupon) * math.exp(-y * cash_flows/yearly_frequency)

  return bond_val

def f(y):
  global B_m
  return bond_value(y) - B_m

def df(y):
  global coupon, face_val, cash_flows, B_m, yearly_frequency
  bond_val = 0
  for i in range (1, cash_flows):
    bond_val = bond_val + coupon * (i/yearly_frequency) * math.exp(-y * i/yearly_frequency)

  # maturity
  bond_val = bond_val + (face_val + coupon) * (cash_flows/yearly_frequency) * math.exp(-y * cash_flows/yearly_frequency)

  return -1 * bond_val

def convexity(y, B):
  global coupon, face_val, cash_flows
  bond_val = 0
  for i in range (1, cash_flows):
    bond_val = bond_val + coupon * (i/yearly_frequency)**2 * math.exp(-y * i/yearly_frequency)

  # maturity
  bond_val = bond_val + (face_val + coupon) * (cash_flows/yearly_frequency)**2 * math.exp(-y * cash_flows/yearly_frequency)

  return bond_val/B


coupon = 2
face_val = 100
cash_flows = 8
# B_m = 101
yearly_frequency = 4

# bond_yield = newton_method(f, df, 0.1, 1e-6)

bond_yield = 0.09
bond_val = bond_value(bond_yield)
modified_duration = -1 * df(bond_yield) / bond_val
bond_convexity = convexity(bond_yield, bond_val)

bond_val, bond_yield, modified_duration, bond_convexity
