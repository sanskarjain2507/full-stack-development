y=3
def func():
    x=7
    global y
    y=7
    return y

def func2():
    pass
    # print(x) not defined so error

# print(x) not defined so error

print(y)
print(func())
print(y)
