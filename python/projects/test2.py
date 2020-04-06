a=[]
sum=0
for i in range(0,5):
    c=input(f"enter marks in subject {i+1} -> ")
    c=int(c)
    a.append(c)
    sum+=a[i]
avg=sum/5
if avg>90:
    grade='A'
elif avg>80:
    grade='B'
elif avg>70:
    grade='C'
elif avg>60:
    grade='D'
elif avg>50:
    grade='E'
else:
    grade='F'

if avg<=50:
    print("Student is fail")
else:
    print(f"Total marks is {sum} \n average is {avg} \n garde is {garde}")
