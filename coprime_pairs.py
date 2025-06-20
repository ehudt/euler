from collections import deque


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

