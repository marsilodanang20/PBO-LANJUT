class PersegiPanjang:
    def __init__(self):
        self.panjang = None
        self.lebar = None
        self.luas_permukaan = None
        self.luas = None
        
    @property
    def panjang(self):
        return self._panjang
    
    @panjang.setter
    def panjang(self, value):
        self._panjang = value
        
    @property
    def lebar(self):
        return self._lebar
    
    @lebar.setter
    def lebar(self, value):
        self._lebar = value
        
    def hitung_luas_permukaan(self):
        self.luas_permukaan = 2 * (self._panjang * self._lebar + self._panjang * self._lebar + self._lebar * self._panjang)
        return self.luas_permukaan
    
    def hitung_luas(self):
        self.luas = self._panjang * self._lebar
        return self.luas
    
persegi_panjang = PersegiPanjang()

panjang = float(input("Masukkan panjang persegi panjang: "))
lebar = float(input("Masukkan lebar persegi panjang: "))

persegi_panjang.panjang = panjang
persegi_panjang.lebar = lebar

luas_permukaan = persegi_panjang.hitung_luas_permukaan()
luas = persegi_panjang.hitung_luas()

print("Panjang persegi panjang:", panjang)
print("Lebar persegi panjang:", lebar)
print("Luas permukaan persegi panjang:", luas_permukaan)
print("Luas persegi panjang:", luas)
