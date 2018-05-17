# Solution to https://projecteuler.net/problem=9
for a in range(1,1000//3):
    for b in range(a,1000-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print(a,b,c, a+b+c, a*b*c)