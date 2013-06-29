# problem 93

def EnumerateAllBinaryTrees(n):
  """Enumerate all binary trees of size n."""
  if n == 0:
    yield []
  for i in xrange(n):
    for left_child in EnumerateAllBinaryTrees(i):
      for right_child in EnumerateAllBinaryTrees(n - i - 1):
        yield [left_child, right_child]

import operator
import itertools

operators = [operator.__add__, 
             operator.__sub__, 
             operator.__mul__, 
             operator.__div__]

def EnumerateArithmeticExpressions(numbers):
  """Enumerate all arithmetic expressions with n numbers.

  Args:
    numbers: An iterable of numbers. Must contain n numbers.
  """
  # n is the size of the expression tree
  n = 2 * len(numbers) - 1
  #num_loop = itertools.cycle(numbers)
  def helper(n, numbers):
    if n == 1:
      yield float(numbers[0])
    for i in xrange(1, n - 1, 2):
      for left_child in helper(i, numbers[:(i+1)/2]):
        for right_child in helper(n - i - 1, numbers[(i+1)/2:]):
          for op in operators:
            yield [op, left_child, right_child]
  return helper(n, numbers)

def EvalExprTree(tree):
  if type(tree) is float:
    return tree
  else:
    op = tree[0]
    return op(EvalExprTree(tree[1]), EvalExprTree(tree[2]))

def main():
  expr_size = 4
  max_range = 0
  max_quadruple = ()
  for quadruple in itertools.combinations(range(10), expr_size):
    feasible = set()
    for perm in itertools.permutations(quadruple):
      for expr in EnumerateArithmeticExpressions(perm):
        try:
          result = EvalExprTree(expr)
        except ZeroDivisionError:
          continue
        if result == int(result):
          feasible.add(int(result))
    last_index = 1
    while last_index in feasible:
      last_index += 1
    last_index -= 1
    if last_index > max_range:
      max_range = last_index
      max_quadruple = quadruple
  print max_quadruple, max_range

if __name__ == '__main__':
  main()
