def cube(n):
    c={}
    for i in range(1,n+1):
        c[i]=i**3
    return c

b=cube(10)
print(b)
