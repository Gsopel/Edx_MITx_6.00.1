def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    while a != b:
        if a < b:
            b = b - a
        else:
           a = a - b
    return a





print(gcdIter(17, 12))