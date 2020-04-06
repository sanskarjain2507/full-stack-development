a=eval(input("enter any number to check prime or not"))
i=1
f=0
count=0
while i<a:
    if(a%i==0):
        count+=1

    if count>1:
        f=1
        break
    i+=1

if(f==1):
    print("not a prime number")
else:
    print("prime number")
