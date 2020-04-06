user2 ={
        'name':'sanskar jain',
        'age':20,
        'learning now':['programming','living','engg'],
        }
d=dict.fromkeys(['name','age','height'],'unknown')
print(d)
d=dict.fromkeys("abc",'unknown')
print(d)
print(user2.get('name'))
print(user2.get('names'))

d.clear()
print(d)
us1=user2.copy()
print(us1)
print(us1 is user2)
u1=user2
print(u1 is user2)
print(user2.get('name1','not found'))
user2 ={
        'name':'sanskar jain',
        'age':20,
        'learning now':['programming','living','engg'],
        'name':'samins'
        }
print(user2)
