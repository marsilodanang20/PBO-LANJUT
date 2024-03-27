class Buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        
    def info(self):
        print(f"Judul Buku: {self.judul}\nPengarang: {self.pengarang}\nTahun Terbit: {self.tahun_terbit}")


buku1 = Buku("Dilan 1990", "Pidi Baiq", 2018)
buku1.info()