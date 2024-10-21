# bond zero rate bootstrapping calculation using newtons'method in the conncurrent approximation under tolerance
import math

def newtons_method(f, df, initial_guess, tol=1e-6):
    x_current = initial_guess
    iteration_count = 0
    while True:
        f_value = f(x_current)
        df_value = df(x_current)
        x_next = x_current - f_value / df_value
        iteration_count += 1
        print(f"Iteration {iteration_count}: {x_next}")
        if abs(x_next - x_current) < tol:
            break
        x_current = x_next
    return x_current, iteration_count

# Example usage
# result, iteration_count = newtons_method('x**2 - 2*x - 3', '2*x - 2', 3.0, 1e-6)
# print(f"The root is approximately at x = {

def f(y):
  three_year_rate = 0.042118
  x = three_year_rate

  r_arr = [0, 0.050636, 0.049370, 0.25 * x + 0.037028, 0.5 * x + 0.024685, 0.75 * x + 0.012343, x,
           0.25*y + x*0.75, 0.5*y + x*0.5, 0.75*y + 0.25 * x, y]

  c_arr = [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 103]
  t_arr = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

  print(len(r_arr), len(c_arr), len(t_arr))
  sum = 0
  for i in range(1, len(r_arr)):
    sum = sum + c_arr[i]  * math.exp(-1 * r_arr[i] * t_arr[i])

  return sum - 104

def df(y):
  three_year_rate = 0.042118
  x = three_year_rate

  r_arr = [0, 0.050636, 0.049370, 0.25 * x + 0.037028, 0.5 * x + 0.024685, 0.75 * x + 0.012343, x,
           0.25*y + x*0.75, 0.5*y + x*0.5, 0.75*y + 0.25 * x, y]

  c_arr = [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 103]
  t_arr = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
  print(len(r_arr), len(c_arr), len(t_arr))
  diff_arr = [0, 0, 0, 0, 0, 0, 0, -0.25 * 3.5, -0.5 * 4, -0.75 * 4.5, -5]

  sum = 0
  for i in range(1, len(r_arr)):
    sum = sum + c_arr[i] * diff_arr[i] * math.exp(-1 * r_arr[i] * t_arr[i])

  return sum

def calculate():
  three_year_rate = 0.042118
  x = three_year_rate

  five_year_rate = 0.050826
  y = five_year_rate
  return 0.25*y + x*0.75, 0.5*y + x*0.5, 0.75*y + 0.25 * x


bond_zero_rate, iterations = newtons_method(f, df, 0.05, 1e-6)

bond_zero_rate, iterations, calculate()