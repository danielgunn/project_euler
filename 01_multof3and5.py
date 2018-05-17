# Solution to https://projecteuler.net/problem=1
t=0
n=1
for x in 3,5:
    n = 1
    while (x*n < 1000):
        print("x*n",x*n)
        t+=x*n
        print("t",t)
        n+=1
# remove powers of 15
n=1
x=15
while (x*n < 1000):
    print("-x*n",x*n)
    t-=x*n
    n+=1
    print("t",t)