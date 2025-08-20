
# traditional way
def display(a,b):
    c = a + b
    return c

total = display(10,20)
print(total)

# pythonic way
# lambda function : lambda is the replacement of single liner function only
# If cant define lambda if the function body has more no. of lines
#Advantage : expression will be replaced in the calling function
# lambda is faster in terms of execution

#syntax
#functioname = lambda varibales : expression

display = lambda a,b: a + b
total = display(10,20)
print(total)

concat = lambda a,b: a + " " + b
total = concat("python","programming")
print(total)

# Square of a number
square = lambda x: x ** 2
print(square(4))  # 16

#  Length of a string
length = lambda s: len(s)
print(length("python"))  # 6

# Convert to uppercase
upper = lambda s: s.upper()
print(upper("hello"))  # HELLO

# max of two numbers
maximum = lambda a, b: a if a > b else b
print(maximum(10, 20))  # 20

# pass or fail
result = lambda marks: "Pass" if marks >= 35 else "Fail"
print(result(30))  # Fail


#Positive, Negative or Zero
sign = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"
print(sign(-5))  # Negative





alist = [10,20,30]

# write a program to read the above list and display the below output

#[15,25,35]


alist = [10,20,30]
blist = []
for val in alist:
    blist.append(val + 5)
print(blist)


#map(function,iterable)   # function can be builtin function or user defined function or lambda function
print(list(map(lambda  x: x + 5 , alist)))


#Convert to strings
nums = [1, 2, 3, 4, 5]
to_str = list(map(lambda x: str(x), nums))
print(to_str)  # ['1', '2', '3', '4', '5']


#Uppercase names
names = ["alice", "bob", "carol"]
upper_names = list(map(lambda x: x.upper(), names))
print(upper_names)  # ['ALICE', 'BOB', 'CAROL']


#Extract domain from email
emails = ["user1@gmail.com", "user2@yahoo.com"]
domains = list(map(lambda x: x.split("@")[1], emails))
print(domains)


nums =[1,2,3]
to_str = list(map(lambda x: str(x), nums))
print(to_str)


# filter(function,iterable)
alist = ["unix","python","c",'perl',"ruby"]
output = list(filter(lambda x: len(x)==4 , alist))
print(output)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)   # [2, 4, 6, 8]


students = [
    {"name": "Alice", "score": 85},
    {"name": "Bob", "score": 45},
    {"name": "Charlie", "score": 72},
]
passed = list(filter(lambda s: s["score"] >= 50, students))
print(passed)