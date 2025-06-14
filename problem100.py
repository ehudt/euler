from gmpy2 import mpz

r = mpz(1)
limit = mpz(10) ** 12

M = [[mpz(3), mpz(4)], [mpz(2), mpz(3)]]
k_y = [mpz(1), mpz(1)]


def multiply(m, v):
    return [m[0][0] * v[0] + m[0][1] * v[1], m[1][0] * v[0] + m[1][1] * v[1]]


while True:
    k_y = multiply(M, k_y)
    k, y = k_y
    if not k & 1 or not y & 1:
        continue
    n = (1 + k) // 2
    if n < limit:
        continue
    b = (1 + y) // 2
    print('b=', b, 'n=', n)
    break
