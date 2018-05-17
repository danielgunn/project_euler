# Solution to https://projecteuler.net/problem=4
def is_pal(n):
    s = str(n)
    l = len(s)
    for i in range(0,len(s)//2):
        if s[i] != s[-(i+1)]:
            return False
    return True

m = 0
for i in range(100,1000):
    for j in range(100,1000):
        n = i * j
        if (is_pal(n)):
            if (n > m):
                m = n
                print(i,j,n)