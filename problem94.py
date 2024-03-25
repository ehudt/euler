#!/usr/bin/env python3
# encoding: utf-8


def area(a, b, c):
    return a * (b * b - a * a / 4) ** 0.5 / 2


def main():
    print("Problem 94")
    b = 2
    s = 0
    i = 0
    while True:
        for delta in [-1, 1]:
            a = b + delta
            p = a + b + b
            if p > 1000000000:
                continue
            ar = area(a, b, b)
            if ar == int(ar):
                s += p
                if i % 1000000 == 0:
                    print("(a, b, c) = ", (a, b, b), "(p, ar) = ", (p, ar))
        if p > 1000000000:
            break
        b += 1
    print("sum= ", s)


if __name__ == "__main__":
    main()
