def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here

    result = []
    for k, v in aDict.items():
        if v == target:
            result.append(k)
    result.sort()

    return result


aDict = {1:2, 6:4, 5:6, 10:1, 5:4, }

print(keysWithValue(aDict, 4))