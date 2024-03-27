class segitiga:
    def __init__(self):
        self._tinggi = None
        self._alas = None
        
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
         
    def luas(self):
        return 0.5 * self._alas * self._tinggi
     
S = segitiga()
A = input("masukan nilai alas:")
T = input("masukan nilai tinggi:")
    
S.alas = int(A)
S.tinggi = int(T)
    
L = S.luas()
    
print("alas:", A)
print("tinggi:", T)
print("luas:", L)