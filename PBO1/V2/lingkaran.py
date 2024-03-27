class Lingkaran:
    def __init__(self):
        self.jari_jari = None
        self.luas = None
        self.keliling = None
        
    def hitung_luas(self, jari_jari):
        self.jari_jari = jari_jari 
        self.luas = 3.14 * self.jari_jari**2
        return self.luas
    
    def hitung_keliling(self, jari_jari):
        self.jari_jari = jari_jari 
        self.keliling = 2 * 3.14 * self.jari_jari
        return self.keliling
    
lingkaran = Lingkaran()

jari_jari = float(input("Masukkan jari-jari lingkaran: "))

luas = lingkaran.hitung_luas(jari_jari)
keliling = lingkaran.hitung_keliling(jari_jari)

print("Jari-jari lingkaran:", jari_jari)
print("Luas lingkaran:", luas)
print("Keliling lingkaran:", keliling)