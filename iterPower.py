def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    count = 1
    result = 1
    if exp == 0:
        return 1
    else:
        while count <= exp:
            result = result * base
            count += 1
        return result
print(iterPower(4,3))