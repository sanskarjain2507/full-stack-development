a=eval(input("enter any number to find armstrong or not"))
n=a
count=0

while n!=0:
    n=n//10
    count+=1


dig=count
n=a
count=0
while n!=0:
    b=n%10
    n=n//10
    count=count+b**dig

if count==a:
    print("the number is armstrong")
else:
    print("the number is not armstrong")
