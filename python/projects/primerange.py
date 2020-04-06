a=eval(input("enter the starting range of prime number"))
b=eval(input("enter the ending range of prime number"))
i=1
f=0
while a<=b:
    n=a
    count=0
    while i<a:
        if(a%i==0):
            count+=1

        if count>1:
            f=1
            break
        i+=1
    if(f==0):
        print(a,end=" ")
    i=1
    a+=1
    f=0
