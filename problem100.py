import gmpy2
# import math

# # n=1004114331515, b=710016052901
# r=1
# while True:
#     r+=1
#     q=r**2
#     p=int((2*q**2-1)**.5)
#     qtag = int(((p**2+1)/2)**.5)
#     if qtag != q:
#         continue
#     n = (1+p)/2
#     if n != math.floor(n):
#         continue
#     n = int(n)
#     b=(1+(1+2*n*(n-1))**.5)/2
#     if b != math.floor(b):
#         continue
#     if n >= 10**12:
#         print(f'n={n}, b={b}, p={p}, q={q}, r={r}')
#         break
    

r     = gmpy2.mpz(1)
limit = gmpy2.mpz(10)**12

while True:
    r += 1
    q = r * r
    # print q every many iterations
    if r % 1000000 == 0:
        print('r=', r, 'q=', q)
    p2 = 2 * q * q - 1
    if not gmpy2.is_square(p2):
        continue
    p = gmpy2.isqrt(p2)
    # check qtag^2 = (p^2+1)/2
    qtag2 = (p*p + 1) // 2
    if not gmpy2.is_square(qtag2):
        continue
    qtag = gmpy2.isqrt(qtag2)
    if qtag != q:
        continue

    # n = (1+p)/2 must be integer
    if (1 + p) & 1:
        continue
    n = (1 + p) // 2
    if n < limit:
        continue

    # b = (1 + sqrt(1 + 2n(n-1))) / 2 must be integer
    T = 1 + 2*n*(n-1)
    if not gmpy2.is_square(T):
        continue
    b_num = 1 + gmpy2.isqrt(T)
    if b_num & 1:
        continue
    b = b_num // 2
    print(f'n={n}, b={b}, p={p}, q={q}, r={r}')
    break

# n=gmpy2.mpz(10)**12
# while True:
#     if n%1000000 == 0:
#         print('n=',n)
#     q2 = 2*n*(n-1)+1
#     if not gmpy2.is_square(q2):
#         n+=1
#         continue
#     q = gmpy2.isqrt(q2)
#     b = (1+q)/2
#     print('b=',b, 'n=',n)
#     break