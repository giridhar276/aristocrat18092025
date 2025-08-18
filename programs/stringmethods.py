
# slicing
name = "python programming"
#print(name[18])
#slicing

#string[start:stop:step]
print(name)
print(name[0]) #p
print(name[1]) #y
print(name[0:4]) #pyth
print(name[9:14]) #ogram
print(name[0:18]) #python programming
print(name[0:18:1]) #python programming
print(name[0:18:2])
print(name[0:18:2]) #pto rgamn
print(name[0:18:3]) #ph oai
print(name[:])  #python programming
print(name[0:18:1]) #python programming
print(name[::1])#python programming
print(name[-1]) #g
print(name[-4:-1])
print(name[::3])
print(name[::-1])# 
print(name[-5:-11:-1])



name = "python programming"
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())
print(name.isupper())
print(name.islower())
print(name.isalpha())
print(name.isalnum())
print(name.center(40))
print(name.center(40,"*"))
print(name.count('p'))  # no. of occurences of the substring
print(name.count('prog'))
print(name.count('ja'))

print(name.find("prog")) # existence of substring
print(name.find("abc"))  # if the output is -1 substring is not found.
print(name.split(" "))
print(name.startswith("p")) # True
print(name.startswith("g")) # False
print(name.endswith("g"))
print(name.endswith("m"))
aname = " python   "
print(len(aname))
print(len(aname.strip()))  # will remove whitespaces at both ends
print(len(aname.lstrip()))
print(len(aname.rstrip()))
aname = "I love {} and {}" # string template  # string is defined only once
print(aname.format("Delhi","Hyderabad"))
print(aname.format("java","unix"))
print(aname.format("UK","US"))

aname = "I love {1} and {0}" # string template  # string is defined only once
print(aname.format("Delhi","Hyderabad"))
print(aname.format("java","unix"))
print(aname.format("UK","US"))


name = "python programming"
print(name.isprintable())
name = "python\nprogramming"
print(name.isprintable())


# conditions
if 1 < 2 :
    print("true")
else:
    print("false")

## simple if
name = "python"
if name.islower() :
    print("string is string")
    print("inside if")
    print("still inside if")

#if-else
name = "python"
if name.islower():
    print("string is string")
else:
    print("string is upper")

# if-elif-elif-elif-else 
name = input("Enter any language:")
print("You entered :", name )
if name == "python":
    print("you entered python")
elif name == "java":
    print("you entered java")
elif name == "unix":
    print("you entered unix")
else:
    print("its someother unknown language")


name = input("Enter any value:")

print(type(name))
print(isinstance(name,str)) # True
print(isinstance(name,list)) # False


name = "python programming"
if name.find("prog") != -1 :
    print("substring found")

# easiest way to check substring exists or not.
if 'prog' in name:
    print("substring found")
else:
    print("not found")


alist = [10,20,30]
if 30 in alist:
    print("value found")



name = "python"
for char in name:
    print(char)

# range(start,stop,step)
for val in range(1,5):
    print(val)

for val in range(5,0,-1):
    print(val)

alist = [10,20,30]
for val in alist:
    print(val)


print(10,20,end="\n")
print(30)