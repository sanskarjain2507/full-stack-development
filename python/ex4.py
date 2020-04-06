name,ch=input("enter your name and any letter").split(",")
print(f"length of your name is {len(name)} and number of {ch} in your name is {name.count(ch.lower())+name.count(ch.upper())}")
print(f"{name.lower().count(ch.lower())}")#or we can also do in this way
print(f"{name.strip().lower().count(ch.strip().lower())}")
