# Solution to https://projecteuler.net/problem=3
n = 600851475143 
p = 2
l = 1
while (n > 1):
    if (n % p) == 0:
        n = n / p
        print(n)
        l = p
    else:
        p = p + 1
print(l)