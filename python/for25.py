#1234->1+2+3+4
total=0
num=input("enter a number")
for i in range(0,len(num)):
    total+=int(num[i])

print(total)
