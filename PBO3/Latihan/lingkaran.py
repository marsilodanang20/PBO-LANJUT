import math

class Lingkaran:
    def __init__(self, jari_jari):
        self.__set_jari_jari(jari_jari)

    def get_jari_jari(self):
        return self.__jari_jari

    def __set_jari_jari(self, nilai):
        self.__jari_jari = 1 if nilai <= 0 else nilai

    def luas_permukaan(self):
        return math.pi * (self.__jari_jari ** 2)

    def keliling(self):
        return 2 * math.pi * self.__jari_jari

try:
    jari_jari = float(input("Masukkan panjang jari-jari lingkaran: "))
except ValueError:
    print("Masukkan hanya angka saja.")
else:
    lingkaran = Lingkaran(jari_jari)
    luas_permukaan = lingkaran.luas_permukaan()
    keliling = lingkaran.keliling()
    print("Jari-jari Lingkaran:", lingkaran.get_jari_jari())
    print("Luas Permukaan Lingkaran:", luas_permukaan)
    print("Keliling Lingkaran:", keliling)
