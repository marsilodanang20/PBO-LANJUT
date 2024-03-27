class JajarGenjang:
    def __init__(self):
        self.alas = None
        self.tinggi = None
        self.tinggi_sejajar = None
        self.luas = None
        
    def hitung_luas(self, alas, tinggi, tinggi_sejajar):
        self.alas = alas 
        self.tinggi = tinggi
        self.tinggi_sejajar = tinggi_sejajar
        self.luas = self.alas * self.tinggi_sejajar
        return self.luas
    
jg = JajarGenjang()

alas = float(input("Masukkan alas jajar genjang: "))
tinggi = float(input("Masukkan tinggi jajar genjang: "))
tinggi_sejajar = float(input("Masukkan tinggi sejajar jajar genjang: "))
luas = jg.hitung_luas(alas, tinggi, tinggi_sejajar)

print("Alas:", alas)
print("Tinggi:", tinggi)
print("Tinggi Sejajar:", tinggi_sejajar)
print("Luas Jajar Genjang:", luas)
