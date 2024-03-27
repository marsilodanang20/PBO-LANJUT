class Pegawai:
    def __init__(self, nama, jabatan, gaji):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji = gaji
        
    def info(self):
        print(f"Nama: {self.nama}\nJabatan: {self.jabatan}\nGaji: {self.gaji}")


pegawai1 = Pegawai("Jamaludin", "Manajer", 5000000)
pegawai1.info()
