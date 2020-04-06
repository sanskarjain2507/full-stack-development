s={'a','b'}

if 'a' in s:
    print("present")

for i in s:
    print(s)

s1={1,2,3,4}
s2={3,4,5,6}
#union
u=s1 | s2
print(u)

#intersection
inter = s1 & s2
print(inter)
