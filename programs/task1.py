

'''

write a program to reverse a string without using [::-1]

Enter any string:  python
nohtyp

'''


text = input("Enter any string :")
revtext = ""

for char in text:
    revtext = char + revtext
print("String reverse:", revtext)



text = input("Enter any string :")
data = list(text)   #["p","y","t","h","o","n"]
data.reverse()      #["n","o","h","t","y","p"]
string = "".join(data)     #nohtyp
print(string)