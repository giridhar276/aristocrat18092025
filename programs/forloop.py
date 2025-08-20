
# range(start,stop,step)
for val in range(1,5):
    print(val)


for val in range(5,0,-1):
    print(val)

# string
name = "python"
for char in name:
    print(char)

# list
alist = [10,20,30,40]
for val in alist:
    print(val)

for val in alist[::-1]:
    print(val)

alist = [10,20,30,40]
alist.reverse()
for val in alist:
    print(val)


book = {"chap1":10,"chap2":20}
for key,value in book.items():
    print(key)
    print(value)

aset = {10,10,10,20,20,30,30}
for val in aset:
    print(val)