def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    test = len(aStr)
    if aStr == '':
        return False
    elif test == 1:
        return char == aStr
    elif char == aStr[test//2]:
        return True
    else:
        return isIn(char, aStr[test // 2: ]) or isIn(char, aStr[ : test // 2])




print(isIn( 'b' ,'barburka'))