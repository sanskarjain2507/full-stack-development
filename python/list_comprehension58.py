squares=[]
for i in range(1,11):
    squares.append(i**2)

print(squares)

square2 = [i**2 for i in range(1,11)]
print(square2)

names=['sanskar','adi']
new_list = [name[0] for name in names]
print(new_list)

l=list(range(1,11))
l1=[i for i in l if i%2==0] #to print even numbers
print(l1)
