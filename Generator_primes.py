def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i= 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 1
    return True

def genPrime():
    item = 0
    while True:
        if is_prime(item) == True:
            yield item

        item +=1

prim = genPrime()



