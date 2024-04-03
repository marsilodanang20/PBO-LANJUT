class BelahKetupat:
    def __init__(self, diagonal1, diagonal2):
        self.__set_diagonal1(diagonal1)
        self.__set_diagonal2(diagonal2)

    def get_diagonal1(self):
        return self.__diagonal1

    def get_diagonal2(self):
        return self.__diagonal2

    def __set_diagonal1(self, nilai):
        self.__diagonal1 = 1 if nilai <= 0 else nilai

    def __set_diagonal2(self, nilai):
        self.__diagonal2 = 1 if nilai <= 0 else nilai

    def luas_permukaan(self):
        return self.__diagonal1 * self.__diagonal2

try:
    diagonal1 = float(input("Masukkan panjang diagonal pertama belah ketupat: "))
    diagonal2 = float(input("Masukkan panjang diagonal kedua belah ketupat: "))
except ValueError:
    print("Masukkan hanya angka saja.")
else:
    belah_ketupat = BelahKetupat(diagonal1, diagonal2)
    luas_permukaan = belah_ketupat.luas_permukaan()
    print("Diagonal Pertama Belah Ketupat:", belah_ketupat.get_diagonal1())
    print("Diagonal Kedua Belah Ketupat:", belah_ketupat.get_diagonal2())
    print("Luas Permukaan Belah Ketupat:", luas_permukaan)
