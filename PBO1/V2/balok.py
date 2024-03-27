class Balok:
    def __init__(self):
        self.panjang = None
        self.lebar = None
        self.tinggi = None
        self.volume = None
        
    def hitung_volume(self, panjang, lebar, tinggi):
        self.panjang = panjang 
        self.lebar = lebar
        self.tinggi = tinggi
        self.volume = self.panjang * self.lebar * self.tinggi
        return self.volume
    
b = Balok()

panjang = float(input("Masukkan panjang balok: "))
lebar = float(input("Masukkan lebar balok: "))
tinggi = float(input("Masukkan tinggi balok: "))
volume = b.hitung_volume(panjang, lebar, tinggi)

print("Panjang:", panjang)
print("Lebar:", lebar)
print("Tinggi:", tinggi)
print("Volume Balok:", volume)