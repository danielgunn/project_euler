# Solution to https://projecteuler.net/problem=7

primes = []
n = 1

def is_prime(n):
    for p in primes:
        if n % p == 0:
            return False
    return True


while(len(primes) < 10001):
    n += 1 
    if is_prime(n):
        primes.append(n)
        print(len(primes),n)
print(primes.pop())