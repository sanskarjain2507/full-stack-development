def rev_list(l):
    l1=[]
    for i in range(len(l)):
        l1.append(l.pop())
    return l1

print(rev_list([1,2,3,4,5,6,7,8,9]))

#or
l=[1,2,3,4,5,6,7,8,9]
l.reverse()
print(l)

#or

def rev_list1(l):
    return l[::-1]

l2=rev_list(l)
print(l2)
