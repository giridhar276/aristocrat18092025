
#method1
#file object acts like an handler
#- read the file line by line using file object
with open("language1111s.csv","r") as fobj:
    for line in fobj:
        print(line.strip())


#method2
# display in the form of the list
with open("languages.csv","r") as fobj:
    print(fobj.readlines())

#method3
# display in the form of the string
# not suggested for bigger files
with open("languages.csv","r") as fobj:
    print(fobj.read())

#method4

import csv
with open("languages.txt","r") as fobj:
    # converting file object to csv understandable object
    reader = csv.reader(fobj)
    for line in reader:
        print(line)

#method5
import pandas as pd
df = pd.read_csv("languages.csv")
print(df)
