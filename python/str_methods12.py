print(len("sanskar"))
name="Sanskar JAIN"
print(name.lower())

name="Sanskar jain"

print(name.upper())
print(name.title())
print(name.count("Sa"))
name="    sans    kar        "
dots=".........."
print(name+dots)
print(name.lstrip()+dots)
print(name.rstrip()+dots)
print(name.strip()+dots)
print(name.replace(" ","")+dots)
print(name.replace(" ","-"))
print(name.replace(" ","-",2))
print(name.find("k"))
name="sanskar"
print(name.center(9,"*"))
name=input("enter your name")
print(name.center(len(name)+8,"*"))
