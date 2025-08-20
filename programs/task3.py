

'''
wrrite a program to reverse a list without list.reverse() and [::-1]



'''


alist = [45,56,32,67,32,65,63]
revlist = []

for val in alist:
    revlist = [val] + revlist

print("after reversing :", revlist)