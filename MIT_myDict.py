class myDict(object):
    """ Implements a dictionary without using a dictionary """

    def __init__(self):
        """ initialization of your representation """
        self.dictionary = []

    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        self.k = k
        self.v = v
        isThere = False
        if len(self.dictionary) == 0:
            self.dictionary += [[k, v]]
            isThere = True

        for item in self.dictionary:
            if k == item[0]:
                item[1] = v
                isThere = True

        if isThere == False:
            self.dictionary += [[k, v]]

    def getval(self, k):
        for item in self.dictionary:
                if item[0] == k:
                    return item[1]
        raise KeyError

    def delete(self, k):
        """ k, immutable object """
 #       try:
        count = False
        for item in self.dictionary:
            if k == item[0]:
                del item[:]
                self.dictionary = [x for x in self.dictionary if x != []]
                count = True
        if count == False:
            raise KeyError


    def drukuj(self):
        return print(self.dictionary)

d1 = myDict()
d2 = myDict()
d1.assign(10, 2)
print(d1.getval(10))
d1.assign(3, 3)
print(d1.getval(3))
print(d1.getval(10))
d1.assign(4, 2)
print(d1.getval(4))
d1.assign(3, 6)
print(d1.getval(3))
print(d1.getval(10))
print(d1.getval(3))
print(d1.getval(4))
d1.delete(3)
d1.delete(10)
print(d1.getval(4))






