# Return TAK if number is prime, NIE if is not

def is_prime():
    proby = int(input())
    liczby = []
    while proby > 0:
        liczba = int(input())
        liczby.append(liczba)
        proby -= 1

    for item in liczby:
        if check_prime(item) == True:
            print("TAK")
        else:
            print("NIE")

def check_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 4
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
            break
        i += 1
    return True

is_prime()



