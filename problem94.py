#!/usr/bin/env python3
import gc
from tqdm import tqdm
from gmpy2 import mpfr, sqrt
import gmpy2

ctx = gmpy2.get_context()
ctx.precision = 128

limit = 1000000000


def check_area(a, b2):
    b = b2 / 2
    c = sqrt(a * a - b * b)
    area = mpfr(b * c)
    if area.is_integer() and a + a + b2 <= limit:
        return a + a + b2
    return 0


def main():
    s = 0
    for a in tqdm(range(limit // 3 + 10), desc="Processing"):
        s += check_area(a, a - 1)
        s += check_area(a, a + 1)
    print(s)


if __name__ == "__main__":
    main()
