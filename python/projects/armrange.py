dig=1
count=0
j=10
i=0
while i<5:
    n=j
    while n!=0:
        a=n%10
        n=n//10
        count=count+a**(dig)
    if(count==j):
        print(j,end=" ")
        i+=1
    count=0
    j+=1
    if j%(10**dig)==0:
        dig+=1
