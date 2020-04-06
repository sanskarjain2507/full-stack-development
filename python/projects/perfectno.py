a=eval(input("enter any number to check perfect or not"))
i=1

n=a
sum=0
while i<a:
    if(a%i==0):
        sum+=i
    i+=1

if(n==sum):
    print("it is a perfect number")
else:
    print("it is not a perfect number")
