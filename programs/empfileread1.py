###### using set
import csv
unique_workclasses = set()
with open("empinfo.csv") as fobj:
    header = fobj.readline()
    reader = csv.reader(fobj)
    # processing
    for line in reader:
        workclass = line[1]
        #print(workclass)
        unique_workclasses.add(workclass)
    # displaying
    for work in unique_workclasses:
        print(work)

#### using dict
import csv
uniquedict = dict()
with open("empinfo.csv") as fobj:
    header = fobj.readline()
    reader = csv.reader(fobj)
    # processing
    for line in reader:
        workclass = line[1]
        #print(workclass)
        uniquedict[workclass] = 1    # {"Self-emp-inc":1 ,"Local-gov":1,"Private":1}
        #uniquedict["private"] =1    # {"private":1}
        #uniquedict["federal"] = 1
    # displaying
    for work in uniquedict:
        print(work)



