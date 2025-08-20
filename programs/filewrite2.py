



fobj = open("data.txt","w")   # will be created in current working directory
fobj.write("unix\n")
fobj.write("java\n")
fobj.write("genai\n")
fobj.writelines(["c","cpp","java\n"])
fobj.close()



#### context manager : If any line starts using with keyword ... it is treated as context manager
#### Advantage : file is closed automatically

with open("data.txt","w") as fobj:
    fobj.write("unix\n")
    fobj.write("java\n")
    fobj.write("genai\n")
    fobj.writelines(["c","cpp","java\n"])
    print(fobj.closed) #False

print(fobj.closed)  # True


# opening server connection
# db connections
# socket connection