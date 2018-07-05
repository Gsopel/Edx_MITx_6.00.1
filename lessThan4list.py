def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    bList = []
    for item in aList:
        if len(item) <= 3:
            bList.append(item)
    return bList







aList = ['He', 'hDyZUNCzV', 'eTBrcSoEj', 'rXLe', 'kSwc', 'uCjVcqtYf', 'outbAzx', 'RcBbI']

print(lessThan4(aList))