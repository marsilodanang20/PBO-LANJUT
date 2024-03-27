class Trapesium:
    def __init__(self):
        self.sisi_atas = None
        self.sisi_bawah = None
        self.tinggi = None
        self.sisi_miring = None
        self.luas_permukaan = None
        
    @property
    def sisi_atas(self):
        return self._sisi_atas
    
    @sisi_atas.setter
    def sisi_atas(self, value):
        self._sisi_atas = value
        
    @property
    def sisi_bawah(self):
        return self._sisi_bawah
    
    @sisi_bawah.setter
    def sisi_bawah(self, value):
        self._sisi_bawah = value
        
    @property
    def tinggi(self):
        return self._tinggi
    
    @tinggi.setter
    def tinggi(self, value):
        self._tinggi = value
        
    @property
    def sisi_miring(self):
        return self._sisi_miring
    
    @sisi_miring.setter
    def sisi_miring(self, value):
        self._sisi_miring = value
        
    def hitung_luas_permukaan(self):
        self.luas_permukaan = 0.5 * (self._sisi_atas + self._sisi_bawah) * self._tinggi + self._sisi_miring
        return self.luas_permukaan
    
trapesium = Trapesium()

sisi_atas = float(input("Masukkan panjang sisi atas trapesium: "))
sisi_bawah = float(input("Masukkan panjang sisi bawah trapesium: "))
tinggi = float(input("Masukkan tinggi trapesium: "))
sisi_miring = float(input("Masukkan panjang sisi miring trapesium: "))

trapesium.sisi_atas = sisi_atas
trapesium.sisi_bawah = sisi_bawah
trapesium.tinggi = tinggi
trapesium.sisi_miring = sisi_miring

luas_permukaan = trapesium.hitung_luas_permukaan()

print("Sisi atas trapesium:", sisi_atas)
print("Sisi bawah trapesium:", sisi_bawah)
print("Tinggi trapesium:", tinggi)
print("Sisi miring trapesium:", sisi_miring)
print("Luas permukaan trapesium:", luas_permukaan)
