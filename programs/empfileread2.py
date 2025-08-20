
import csv
mcount = 0
fcount = 0
with open("empinfo.csv") as fobj:
    header = fobj.readline()

    reader = csv.reader(fobj)
    # processing
    for line in reader:
        gender = line[9].strip()
        if gender == "Male":
            mcount+=1
        elif gender == "Female":
            fcount+=1
    print("Total male count  :", mcount)
    print("Total female count:",fcount)

#################################################
import csv
with open("empinfo.csv") as fobj:
    header = fobj.readline()
    reader = csv.reader(fobj)

    # Collect all genders in one list
    genders = list(map(lambda line: line[9].strip(), reader))

    # Count males and females using filter + lambda
    mcount = len(list(filter(lambda g: g == "Male", genders)))
    fcount = len(list(filter(lambda g: g == "Female", genders)))

    print("Total male count  :", mcount)
    print("Total female count:", fcount)
