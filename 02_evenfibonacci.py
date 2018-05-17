# Solution to https://projecteuler.net/problem=2
t1 = 0
t2 = 1
tn = 0
s=0
print(t1)
print(t2)
while t2+t1 <= 4000000:
    tn = t2+t1
    if (tn % 2) == 0:
        s+=tn
    t1 = t2
    t2 = tn
    print(tn)
print(s)
