

atup = (10,20,30,40)

#atup[0] = 100
print(atup)

# casting : converting from one object to another object
atup = (10,20,30,40)
alist = list(atup)   # converting tuple to list
alist.append(50)     # making changes to the list
atup = tuple(alist)  # reconverting back to tuple
print("tuple :", atup)


empdb = [["ram",24],["rita",24],["gita,32"]]   # list of lists



empdb = [("ram",24),("rita",24),("gita,32")]   # list of tuples


