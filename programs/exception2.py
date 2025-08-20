
try:
    with open("languages111.csv","r") as fobj:
        for line in fobj:
            print(line.strip())
except Exception as e:
    print("file is not found.. please check")
    print("system error:",e)


#####################

try:
    with open("languages111.csv","r") as fobj:
        for line in fobj:
            print(line.strip())
except TypeError as err:
    print("INvalid operation")
    print(err)
except ValueError as err:
    print("invalid input")
    print(err)
except (IndexError,KeyError) as err:
    print("INvalid input or invalid key")
    print(err)
except Exception as e:
    print("file is not found.. please check")
    print("system error:",e)

