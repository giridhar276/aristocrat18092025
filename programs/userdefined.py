###### fixed arguments
# function body
def display(a,b):
    c = a + b
    return c
# calling function
total = display(10,20)
print(total)

###### default arguments
def display(a = 0,b = 0,c = 0):
    print(a,b,c)
display()
display(10)
display(10,20)
display(10,20,30)

######## keyword arguments
def display(b,a,c):
    print(a,b,c)
display(c=30,a=10,b=20)

#########variable length arguments
def display(*args):  # *args is the tuple
    print("Sum:",sum(args))
    for val in args:
        print(val)

display(10,20,30,40,50,60,70,80,90)

def displayinfo(**kwargs):  # **kwargs is a dictionary
    for k,w in kwargs.items():
        print(k,w)
displayinfo(chap1_1=10 , chap2_2 = 20)