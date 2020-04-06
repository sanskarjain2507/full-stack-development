def all_total(num1,*args):
    print(args)
    print(num1)
    total=0
    for num in args:
        total+=num
    total+=num1
    return total

print(all_total(1,2,3,4,5,6))
