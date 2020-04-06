bs=eval(input("enter basic salary "))
da=0
hra=0
if bs>=30000:
    da=50
    hra=50
elif bs>=20000:
    da=30
    hra=40
elif bs>=0:
    da=10
    hra=20
da_=bs*da/100
hra_=bs*hra/100
print("Basic Salary ",bs)
print("DA(",da,"%) ", da_)
print("HRA(",hra,"%)",hra_)
print("---------------------------")
print("GROSS SALARY = ",bs+hra_+da_)
