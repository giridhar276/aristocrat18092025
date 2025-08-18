print(3 + 3)  # arithmetic opeator

first = "python"
second = "programming"
final = first + " " + second
print(final)
print(first * 3)
print(final * 3)

alist = [10,20,30]
blist = [40,50,60]
final = alist + blist
print(final)

print(final * 3)

name = "python programming"
if 'prog' in name :
    print("its python programming")

alist = [10,20,30]
if 20 in alist:
    print("value found")

book = {"chap1":10 , "chap2":20}
if "chap1" in book:
    print("key found")

# range(start,stop,step)
for val in range(1,4):
    print(val)