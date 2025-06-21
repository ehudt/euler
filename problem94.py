#!/usr/bin/env python3

import numpy as np
from gmpy2 import mpz, is_square

# def is_square(x):
#     return x == int(x**.5)**2

def main():
    print("Problem 94")
    limit = mpz(1000 * 1000 * 1000)
    s = 0
    x = mpz(1)
    while x + x + x - 1 <= limit:
        # x - 1 case
        if is_square(3 * x - 1) and is_square(x + 1) and x + x + x - 1 <= limit:
            s += x + x + x - 1
        # x + 1 case
        if is_square(3 * x + 1) and is_square(x - 1) and x + x + x + 1 <= limit:
            s += x + x + x + 1
        x += 2
    print(s)


def main2():
    print("Problem 94 with NumPy")
    limit = 1_000_000_000
    s = 0

    x_vals = np.arange(1, int(limit / 3) + 1)
    for delta in [-1, 1]:
        y_vals = x_vals + delta
        perimeter = 3 * x_vals + delta
        valid = perimeter <= limit

        x = x_vals[valid]
        y = y_vals[valid]
        h2 = x * x - (y * y) // 4
        y_even = y % 2 == 0
        h2_four = h2 % 4 == 0

        s += np.sum(perimeter[valid][y_even | h2_four])

    print(s)


if __name__ == "__main__":
    main()
