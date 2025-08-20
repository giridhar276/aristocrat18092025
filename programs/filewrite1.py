



# write operation

fobj = open("data.txt","w")   # will be created in current working directory

# if the file is in different path
#fobj = open("C:\\new\\data.txt","w")
#fobj = open("C:/new/data.txt","w")
#fobj = open(r"C:\new\data.txt","w")  # raw string

fobj.write("unix\n")
fobj.write("java\n")
fobj.write("genai\n")

fobj.writelines(["c","cpp","java\n"])

fobj.close()