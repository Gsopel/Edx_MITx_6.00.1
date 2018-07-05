def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    result = 0
    count = 0
    for num in s:
        if num.isdigit():
            result += int(num)
            count += 1
    if count != 0:
        return result
    else:
        raise ValueError



print(sum_digits("a;asdddasda"))