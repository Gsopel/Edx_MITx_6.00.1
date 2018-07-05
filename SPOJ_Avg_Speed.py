# Avarage speed

def avgSpeed():
    try:
        proby = int(input())
        if 1 <= proby <= 1000:
            for proba in range(proby):
                v1 = int(input())
                v2 = int(input())
                if 1 <= v1 <= 10000 and 1 <= v2 <= 10000:
                    print(int(2*v1*v2 / (v1 + v2)))
                else:
                    raise ValueError
        else:
            raise ValueError
    except ValueError:
        print("Oops!  That was no valid number.")


avgSpeed()