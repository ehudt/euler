#!/usr/bin/env python3
import gc
from tqdm import tqdm
from gmpy2 import mpfr, sqrt
import gmpy2
from concurrent.futures import ProcessPoolExecutor

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


def chunked_range(start, stop, step, chunks):
    chunk_size = (stop - start) // chunks
    for i in range(chunks):
        chunk_start = start + i * chunk_size
        chunk_end = start + (i + 1) * chunk_size if i < chunks - 1 else stop
        yield range(chunk_start, chunk_end, step)


def process_chunk(r):
    s = 0
    for a in r:
        s += check_area(a, a - 1)
        s += check_area(a, a + 1)
    return s


def main():
    num_workers = 8  # Set this to the number of CPU cores you want to use
    start = 0
    stop = limit // 3 + 10
    step = 1
    total = 0
    with ProcessPoolExecutor(max_workers=num_workers) as executor:
        futures = []
        for r in chunked_range(start, stop, step, num_workers):
            futures.append(executor.submit(process_chunk, r))
        for f in tqdm(futures, desc="Processing chunks"):
            total += f.result()
    print(total)


if __name__ == "__main__":
    main()
