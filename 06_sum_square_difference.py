# Solution to https://projecteuler.net/problem=6
t = 0
for i in range(1,101):
    t += i**2
t2 = 0
for i in range(1,101):
    t2 += i
print(t2**2)
print(t)
print(t2**2 - t)