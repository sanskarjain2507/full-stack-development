l1=['abc','def','ghi']

def rev_word(l1):
    l2=[]
    for i in l1:
        l2.append(i[::-1])
    return l2

print(rev_word(l1))
