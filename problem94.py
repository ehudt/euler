#!/usr/bin/env python3

from collections import defaultdict, deque


def coprime_pairs(limit):
    queue = deque()
    queue.append((2, 1))

    def helper():
        while queue:
            m, n = queue.popleft()
            if 2 * m * (m + n) <= limit:
                queue.append((2 * m - n, m))
                queue.append((2 * m + n, m))
                queue.append((m + 2 * n, n))
                yield (m, n)

    return helper()


def vecmul(v, u):
    return sum(x * y for x, y in zip(v, u))


def matmul(A, B):
    return [[vecmul(A[i], B[j]) for j in range(len(B[0]))] for i in range(len(A))]


A = [
    [1, -2, 2],
    [2, -1, 2],
    [2, -2, 3],
]

B = [
    [1, 2, 2],
    [2, 1, 2],
    [2, 2, 3],
]

C = [
    [-1, 2, 2],
    [-2, 1, 2],
    [-2, 2, 3],
]


def all_triples():
    q = deque()
    q.append([[3, 4, 5]])
    while q:
        v = q.popleft()
        yield v[0]
        q.extend(
            [
                matmul(v, A),
                matmul(v, B),
                matmul(v, C),
            ]
        )


def main():
    print("Problem 94")
    limit = 1000 * 1000 * 1000
    s = 0
    for a_, b_, c in all_triples():
        for k in range(1, limit):
            a_, b_, c = a_ * k, b_ * k, c * k
            a = a_ * 2 if a_ % 2 == 1 else b_ * 2
            if not (a + 1 == c or a - 1 == c):
                continue
            if a + c + c > limit:
                break
            s += a + c + c
    print(s)


if __name__ == "__main__":
    main()
