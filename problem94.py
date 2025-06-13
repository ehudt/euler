#!/usr/bin/env python3
# encoding: utf-8

from collections import defaultdict, deque

def coprime_pairs(limit):
    queue = deque()
    queue.append((2,1))
    def helper():
        while queue:
            m, n = queue.popleft()
            if 2 * m * (m + n) <= limit:
                queue.append((2*m-n, m))
                queue.append((2*m+n, m))
                queue.append((m+2*n, n))
                yield (m, n)
    return helper()

def main():
    print("Problem 94")
    limit = 1000*1000*1000
    all_pairs = coprime_pairs(limit)
    # counter = defaultdict(lambda : 0)
    s = 0
    for m, n in all_pairs:
        k = 1
        print(m, n)
        while True:
            a_ = k*(m*m - n*n)
            b_ = k*(2*m*n)
            c = k*(m*m + n*n)
            a = a_*2 if a_%2==1 else b_*2
            if not (a+1 == c or a-1 == c): continue
            if a + c + c > limit: break
            # counter[a+b+c] += 1
            s += a+c+c
            k += 1
    # total = 0
    # for i in range(limit + 1):
    #     if counter[i] == 1:
    #         total += 1
    # print(total)
    print(s)

if __name__ == '__main__':
    main()

    