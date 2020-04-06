l1=[1,2,3,4,5,8]
l2=[1,2,3,7,8,9]
l3=[]
def common(l1,l2):
    for i in l1:
        for j in l2:
            if i==j:
                l3.append(i)

    return l3

print(common(l1,l2))
