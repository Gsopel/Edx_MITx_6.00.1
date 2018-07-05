# Simple adding

import sys

def simple_adding():
    nTests = sys.stdin.readline()
    nTests = int(nTests)
    if 0 < nTests < 100:
        while nTests > 0:
            nNumb = sys.stdin.readline()
            nNumb = int(nNumb)
            suma = 0
            while nNumb > 0:
                liczba = sys.stdin.readline()
                liczba = int(liczba)
                suma += liczba
                nNumb -= 1
            print(suma)
            nTests -= 1
    else:
        return None
simple_adding()
