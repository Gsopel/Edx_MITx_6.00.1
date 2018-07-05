def silnia():
    proby = int(input())
    if 1 <= proby <= 30:
        while proby > 0:
            liczba = input()
            liczba = int(liczba)
            if 0 <= liczba <= 1000000000:
                proby -= 1
                fact = cal_factotial(liczba)
                result = count_decimal(fact)

            else:
                print("Too big number")
def cal_factotial(n):
    result = 1
    while n > 0:
        result = result * n
        n -= 1
    return result

def count_decimal(n):
    if n < 10:
        deci = 0
        jedn = n % 10
        print("{0} {1}".format(deci, jedn))
    else:
        deci = (n % 100) / 10
        jedn = n % 10
        print("{0} {1}".format(int(deci), jedn))

silnia()

