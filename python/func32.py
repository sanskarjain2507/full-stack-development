def last_char(name):
    return name[-1]

print(last_char("sanskar"))


def odd_even(n):
    if n%2==0:
        return "even"
    else:
        return "odd"


print(odd_even(9))
#or
def odd_even(n):
    if n%2==0:
        return "even"
    return "odd"

def is_even(n):
    if n%2==0:
        return True
    else:
        return False

print(is_even(8))

#or

def is_even(n):
    if n%2==0:
        return True

    return False

print(is_even(10))

#or

def is_even(n):
    return n%2==0


print(is_even(9))
