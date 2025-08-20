

import csv
with open("empinfo.csv") as fobj:
    reader = csv.reader(fobj)
    for line in reader:
        print(line)