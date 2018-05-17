# Solution to https://projecteuler.net/problem=5

t = 1
p= 1
for n in range(20,1,-1):
    while (t%n != 0):
        p = 2
        while (True):
            if ((t * p) % n == 0):
                t = t * p
                break
            else:
                p = p + 1
print(t)