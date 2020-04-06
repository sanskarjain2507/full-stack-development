s={1,2,3,1,'sanskar'}
s1=set("sanskar")
print(s1)
print(s)

l=[1,1,2,2,3,4,4,5,5,6,6,5,7,7,'sanskar']
#to remove duplicate
s2 =set(l)
print(s2)
l2=list(s2)
print(l2)
s2.add(8)
print(s2)
s2.remove(8)
print(s2)
s2.clear()
print(s2)
