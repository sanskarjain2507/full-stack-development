a=eval(input("enter any number to print reverse"))
rev=0
b=a
while a!=0:
    n=a%10
    a=a//10
    rev=rev*10+n

print(f"The reverse of entered number is {rev}")

if b==rev:
    print('palindrome')
else:
    print('not a palindrome')
