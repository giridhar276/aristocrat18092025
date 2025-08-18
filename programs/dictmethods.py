
book = {"chap1":10 ,"chap2":20 ,"chap3":30}

print("dictionary :", book)
# add new key-value pairs
book["chap4"] = 40
book["chap5"] = 50
book["chap6"] = 60
print(book)

# display individual values
print(book["chap1"])
print(book["chap2"])
print(book["chap3"])

######## display keys  ##############
print(book.keys())

for key in book.keys():
    print(key)

########### display values #############
print(book.values())

for value in book.values():
    print(value)

############## display items ###########
print(book.items())

for key,value in book.items():
    print(key,value)


##### remove key-value pair
book.pop("chap1")   # chap1-10 will be removed from dictionary
print(book)
book.pop("chap2")   # chap2-20 will be removed from dictionary
print(book)

### remove last key-value pair
book.popitem()
print("After dict.popitem() :", book)
book.popitem()
print("After dict.popitem() :", book)

## combing two dictionaries
# In python **object --> it is treated as dictionary
book = {"chap1":10 ,"chap2":20 ,"chap3":30}
newbook = {"chap4":40 ,"chap5":50}
finalbook = {**book,**newbook}
print("updated book:", finalbook)


book.update(newbook)  # book is updated with newbook
print("updated book:", book)

