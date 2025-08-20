

'''
write a progarm to count character frequencies:


Enter a string :  hello

h : 1 time
e : 1 time
l : 2 times
o : 1 time

'''


text = input("Enter a string:")  #hello

data = set(text)   #{"h","e","l","o"}

for char in data:
    print(char.ljust(5),":",text.count(char),"times")