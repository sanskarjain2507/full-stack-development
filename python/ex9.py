
#modify the guessing game
import random

n=random.randint(1,100)
count=0
while True:
    num= int(input("guess any number between 0 and 100"))
    count+=1
    if(num==n):
        print(f"you win ,you take {count} attempt to guess the number")
        break
    elif(num<n):
        print("too low")
    else:
        print("too high")
