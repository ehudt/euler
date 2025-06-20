#!/usr/bin/env python3

import numpy as np


def main():
    print("Problem 94")
    limit = 1000 * 1000 * 1000
    s = 0
    for x in range(1, limit):
        for y in [x - 1, x + 1]:
            perimeter = x + x + y
            if perimeter > limit:
                print(s)
                return
            h2 = x * x - y * y / 4
            if y % 2 == 0 or h2 % 4 == 0:
                s += perimeter


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
    main2()

