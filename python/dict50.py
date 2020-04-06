user2 ={
        'name':'sanskar jain',
        'age':20,
        'learning now':['programming','living','engg'],
        }

if 'name' in user2:
    print("present")

if 'sanskar jain' in user2.values():
    print('yes')
for i in user2:
    print(i)

u=user2.values()
u1=user2.keys()
print(u,u1)
u3=user2.items()
print(u3)
for key,value in user2.items():
    print(f"key is {key} and value is {value}")
