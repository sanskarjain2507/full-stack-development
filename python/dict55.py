nam=str(input("enter your name"))
print('each word in your name exist as:')
count={}
for i in nam:
    count[i]=nam.count(i)
print(count)
