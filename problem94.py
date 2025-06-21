#!/usr/bin/env python3

import numpy as np
from gmpy2 import mpz, is_square

# def is_square(x):
#     return x == int(x**.5)**2


def main():
    print("Problem 94")
    limit = mpz(1000 * 1000 * 1000)
    s = 0
    x = 1
    while x + x + x - 1 <= limit:
        # x - 1 case
        area1 = ((3 * x - 1) * (x + 1)) // 4 * ((x - 1) * (x - 1) // 4)
        if is_square(area1) and x + x + x - 1 <= limit:
            s += x + x + x - 1
        area2 = ((3 * x + 1) * (x - 1)) // 4 * ((x + 1) * (x + 1) // 4)
        # x + 1 case
        if is_square(area2) and x + x + x + 1 <= limit:
            s += x + x + x + 1
        x += 2
    print(s)


if __name__ == "__main__":
    main()
