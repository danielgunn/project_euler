# Solution to https://projecteuler.net/problem=10
import math

def get_primes(n):
    primes = set(range(2,n))
    p = 2
    factor_limit = math.sqrt(n)
    while (p < factor_limit):
        print(p)
        primes -= set(range(p*2,n,p))
        p+=1
        while (p not in primes) and (p < factor_limit):
            p+=1
    return primes

print(sum(get_primes(2000000)))