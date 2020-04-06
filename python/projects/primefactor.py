a=eval(input("enter any number to find prime factor"))
i=2
while i<=a:
    if a%i==0:
        print(i,end=" ")
        a=a//i
        i=1
    i+=1
