l1=[1,2,3,[1,2],[2,3],[4,5]]
def count_list(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count

print(count_list(l1))
