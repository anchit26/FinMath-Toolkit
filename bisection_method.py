# bisection method
def bisection_method(f, left, right, tol=1e-6, max_iter=100):
  print("***** Running bisection method *****")
  for i in range(1, max_iter + 1):
    x = (left + right)/2
    fx = f(x)
    print("Iteration {}: x = {}, f(x) = {}".format(i, x, fx))
    # stopping criterion
    if abs(fx) < tol:
      print(f'Found solution after {i} iterations.')
      return x

    # reccurence relation
    if fx < 0:
      left = x
    else:
      right = x
  print('Exceeded maximum iterations. No solution found.')
  return None