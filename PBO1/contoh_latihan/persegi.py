class persegi:
    def __init__(self):
        self.panjang = None
        self.lebar = None
        self._luas = None 
    def hitung_luas(self, panjang, lebar):  
        self.panjang = panjang 
        self.lebar = lebar
        self._luas = self.panjang * self.lebar
        return self._luas
    
p = persegi()

panjang = int(input("Masukkan nilai panjang: "))
lebar = int(input("Masukkan nilai lebar: "))
luas = p.hitung_luas(panjang, lebar) 

print("Panjang:", panjang)
print("Lebar:", lebar)
print("Luas:", luas)