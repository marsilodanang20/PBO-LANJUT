class Segitiga:
    def __init__(self):
        self.alas = None
        self.tinggi = None
        self.luas_permukaan = None
        
    @property
    def alas(self):
        return self._alas
    
    @alas.setter
    def alas(self, value):
        self._alas = value
        
    @property
    def tinggi(self):
        return self._tinggi
    
    @tinggi.setter
    def tinggi(self, value):
        self._tinggi = value
        
    def hitung_luas_permukaan(self):
        self.luas_permukaan = 0.5 * self._alas * self._tinggi
        return self.luas_permukaan
    
segitiga = Segitiga()

alas = float(input("Masukkan panjang alas segitiga: "))
tinggi = float(input("Masukkan tinggi segitiga: "))

segitiga.alas = alas
segitiga.tinggi = tinggi

luas_permukaan = segitiga.hitung_luas_permukaan()

print("Alas segitiga:", alas)
print("Tinggi segitiga:", tinggi)
print("Luas permukaan segitiga:", luas_permukaan)
