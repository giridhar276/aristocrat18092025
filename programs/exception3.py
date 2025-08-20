



try:
    fobj = None
    fobj = open("empinfo.csv","r")
except Exception as e:
    print("file is not found.. please check")
    print("system error:",e)
else:
    with fobj:
        for line in fobj:
            print(line.strip())
finally:
    if fobj is not None:
        fobj.close()


