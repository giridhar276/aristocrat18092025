

alist = [67,56,2,4,6,32,7,43,4,66,167,4]
alist.append(92)                  #list.append(value): one single object
print("After appending :",alist)
alist.extend([28,48,2])           #list.extend(alist):  
print("After extending :",alist)
getcount = alist.count(4)
print("4 is repeated for ", getcount ,"times")
alist.insert(0,41)               # list.insert(where,what)   #list.insert(index,value)
print("After inserting :",alist)
alist.insert(6,39)
print("After inserting :",alist)
alist.pop(1)       # 1 is the index       # list.pop(index)   # value at that index is removed
print("After pop operation :",alist)
alist.remove(66)  # 67 is the value in the list
print("After removing :",alist)
alist.sort()   # ascending order
print("After sorting :",alist)
alist.sort(reverse=True)  # descending order
print("sorting in descending :",alist)
alist.reverse()
print("After reversing :",alist)

print(len(alist))
name = "python"
print(len(name))
book = {"chap1":10 ,"chap2":20}
print(len(book))
aset = {10,10,10,20,20,30}
print(len(aset))