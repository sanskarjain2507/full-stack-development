def odd_even(l1):
    l2=[]
    l3=[]
    for i in l1:
        if i%2==0:
            l2.append(i)
        else:
            l3.append(i)
    l4=[]
    l4.append(l2)
    l4.append(l3)
    return l4

print(odd_even([1,2,3,4,5,6,7,8,9]))
