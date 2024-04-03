import math

class Segitiga:
    def __init__(self, alas, tinggi):
        self.__alas = 0
        self.__tinggi = 0
        self.__setAlas(alas)
        self.__setTinggi(tinggi)

    def getAlas(self):
        return self.__alas

    def getTinggi(self):
        return self.__tinggi

    def __setAlas(self, nilai):
        if nilai <= 0:
            self.__alas = 1
        else:
            self.__alas = nilai

    def __setTinggi(self, nilai):
        if nilai <= 0:
            self.__tinggi = 1
        else:
            self.__tinggi = nilai

    def getSisiMiring(self):
        return round(math.sqrt(self.__alas ** 2 + self.__tinggi ** 2), 2)

    def luas(self):
        return 0.5 * self.__alas * self.__tinggi

    def keliling(self):
        return round(self.getSisiMiring() + self.__alas + self.__tinggi, 2)

try:
    alas = int(input("Masukan nilai alas: "))
    tinggi = int(input("Masukan nilai tinggi: "))
except ValueError:
    print("Masukan hanya angka saja")
else:
    p = Segitiga(alas, tinggi)
    L = p.luas()
    k = p.keliling()
    print("Alas:", p.getAlas())
    print("Tinggi:", p.getTinggi())
    print("Luas segitiga:", L)
    print("Keliling segitiga:", k)
