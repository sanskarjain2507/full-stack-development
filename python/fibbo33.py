def fibbo(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n==2:
        print(a, b)
    else:
        print(a, b,end=" ")
        for i in range(0,n-2,1):
            c=a+b
            a=b
            b=c
            print(c,end=" ")

n=int(input("enter the number of terms of fibbonacci series"))
fibbo(n)