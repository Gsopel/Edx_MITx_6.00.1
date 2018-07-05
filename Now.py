def getval(myDict, k):
    for item in myDict:
        if item[0] == k:
            return item[1]
    raise KeyError





myDict = [[1, 2], [3, 4], [5, 6]]

print(getval(myDict,3))