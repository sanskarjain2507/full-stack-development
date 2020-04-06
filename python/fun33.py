def greater(a,b):
    if a>b:
        return a
    return b


def greatest(a,b,c):
    bigger=greater(a,b)
    return greater(bigger,c)

print(greatest(10,20,30))
