class mahasiswa:
    def __init__(self, nama, nim):
        self.nama= nama
        self.nim= nim
        
    def info(self):
        print(f"nama :{self.nama}\nNIM: {self.nim}")
        
mhs = mahasiswa("riski","220511028")
mhs.info()            
       