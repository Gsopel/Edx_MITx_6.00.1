def polysum(n, s):
    from math import tan, pi, pow
    area = (0.25 * (n * pow(s, 2))) / tan(pi / n)
    perimeter = n * s
    suma = area + pow(perimeter, 2)
    return round(suma, 4)



print(polysum(54, 24))