def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result



animals = {'B': [15, 12],'c':[1], 'u': [10, 15, 5, 2, 6], 'h':[1,2,3]}

print(biggest(animals))