# secant method
def secant_method(f, x0, x1, tol=1e-6, max_iter=100):
  print("***** Running secant method *****")
  for i in range(1, max_iter+1):
      fx0 = f(x0)
      fx1 = f(x1)
      print("Iteration {}: x{} = {}, x{} = {}, f(x{}) = {}".format(i, i, x0, i+1, x1, i+1, fx1))
      if abs(fx1 - fx0) < tol:  # Prevent division by a very small number close to zero
          raise ValueError("The function values are too close to each other.")
      if abs(fx1) < tol and abs(x2 - x1) < tol:  # Check if the approximation is within the desired tolerance
          return x1
      x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
      x0, x1 = x1, x2
  raise ValueError("Secant method did not converge")