numbers =list(range(1,11))
print(numbers)

n=numbers.pop()
print(n)

numbers.append(10)
i=numbers.index(3)
print(i)

def neg_list(l):
    negative=[]
    for i in l:
        negative.append(-i)

    print(negative)

neg_list(numbers)
