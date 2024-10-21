# newtons method
def newton_method(f, df, x0, tol=1e-6, max_iter=100):
  print("***** Running Newtons method *****")
  """
  Newton's method for finding roots of f(x)=0.

  Parameters:
  - f : Function for which we are finding roots.
  - df: Derivative of f.
  - x0: Initial guess for a root of f.
  - tol: Tolerance for stopping criterion.
  - max_iter: Maximum number of iterations.

  Returns:
  - xn: Estimated root of the function.
  """
  xn = x0
  for n in range(1, max_iter + 1):
    print("Iteration {}: x = {}".format(n, xn))
    fxn = f(xn)
    print("f(x) = {}".format(fxn))
    if abs(fxn) < tol:
        print(f'Found solution after {n} iterations.')
        return xn
    dfxn = df(xn)
    if dfxn == 0:
        print('Zero derivative. No solution found.')
        return None
    xn = xn - fxn / dfxn
  print('Exceeded maximum iterations. No solution found.')
  return None