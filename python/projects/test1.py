a,b,c =input("enter three numbers ").split()
a=int(a)
b=int(b)
c=int(c)
if a>b and a>c:
    print(f"{a} is greater")
elif b>c:
    print(f"{b} is greater")
else:
    print(f"{c} is greater")
