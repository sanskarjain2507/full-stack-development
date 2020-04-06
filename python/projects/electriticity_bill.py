units=eval(input("enter your units consumed "))
bill=0
if units<=100:
    bill=units*3
elif units>100 and units<=200:
    bill =300+(units-100)*4
elif units>200 and units<=300:
    bill =700 +(units-200)*5
elif units>300:
    bill =1200+(units-300)*6

if bill>1500:
    bill +=(0.15*bill)
print(f"your total bill is {bill} ")
