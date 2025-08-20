try:
    with open("languages111.csv","r") as fobj:
        for line in fobj:
            print(line.strip())
except Exception as e:
    print("file is not found.. please check")
    print("system error:",e)


