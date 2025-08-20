


import time
filename = time.strftime("updatedempinfo_%d_%b_%Y.csv")


with open("empinfo.csv") as fr:
    header = fr.readline()
    with open(filename,"w") as fw:
        fw.write(header)
        for line in fr:
            line = line.replace(" United-States","USA")
            fw.write(line)
            

