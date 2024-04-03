class JajarGenjang:
    def __init__(self, alas, tinggi):
        self.__set_alas(alas)
        self.__set_tinggi(tinggi)

    def get_alas(self):
        return self.__alas

    def get_tinggi(self):
        return self.__tinggi

    def __set_alas(self, nilai):
        self.__alas = 1 if nilai <= 0 else nilai

    def __set_tinggi(self, nilai):
        self.__tinggi = 1 if nilai <= 0 else nilai

    def luas_permukaan(self):
        return self.__alas * self.__tinggi

try:
    alas = float(input("Masukkan panjang alas jajar genjang: "))
    tinggi = float(input("Masukkan tinggi jajar genjang: "))
except ValueError:
    print("Masukkan hanya angka saja.")
else:
    jajar_genjang = JajarGenjang(alas, tinggi)
    luas_permukaan = jajar_genjang.luas_permukaan()
    print("Alas Jajar Genjang:", jajar_genjang.get_alas())
    print("Tinggi Jajar Genjang:", jajar_genjang.get_tinggi())
    print("Luas Permukaan Jajar Genjang:", luas_permukaan)
