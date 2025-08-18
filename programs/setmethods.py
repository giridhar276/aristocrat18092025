
aset = {10,10,20,20,20,30,30,30,30,30}
aset.add(10)
print("after adding :",aset)
aset.add(40)
print("after adding :",aset)

bset = {40,40,40,40,30,30,30,50}

print(aset)
print(bset)

#union
print(aset.union(bset))

#intersection
print(aset.intersection(bset))

#different
print(aset.difference(bset))

#subset
print(aset.issubset(bset))

#superset
print(aset.issuperset(bset))

first = {10,20,30,30,20}
second = {30,30,30,40,50}
first.update(second)
print(first) #{10,20,30,40,50}

#difference
{10,20}