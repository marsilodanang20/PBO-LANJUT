class Persegipanjang :
    def __init__(self,panjang,lebar):
        self.__panjang = 0       # private variabel
        self.__lebar = 0         # private variabel
        self.__setPanjang(panjang)
        self.__setLebar(lebar)
    def getPanjang(sellf):
        return sellf.__panjang
    
    def getLebar(self):
        return self.__lebar
    
    def __setPanjang(self,nilai):
        if(nilai<=0):
            nilai = 1
        self.__panjang = nilai
    
    def __setLebar(self,nilai):
        if(nilai<=0):
            nilai = 1
        self.__lebar = nilai
        
    def Luas(self):
        L = self.__panjang * self.__lebar
        return L
    
    def keliling(self):
        k = (2 * self.__panjang)+(2 * self.__lebar)
        return k
try:
    panjang = int(input("Masukkan nilai panjang:"))
    lebar = int(input("Masukkan nilai lebar:"))
except ValueError:
    print("Masukkan hanya angka")
else:
    p = Persegipanjang(panjang,lebar)
    L = p.Luas()
    k = p.keliling()
    print("Panjang:",p.getPanjang()) 
    print("Lebar:",p.getLebar())
    print("Luas Persegipanjang:,L")
    print("Keliling Persegipanjang:",k)       
        