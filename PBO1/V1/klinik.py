class RekamMedis:
    def __init__(self, nama_pasien, umur, diagnosa):
        self.nama_pasien = nama_pasien
        self.umur = umur
        self.diagnosa = diagnosa
        
    def info(self):
        print(f"Nama Pasien: {self.nama_pasien}\nUmur: {self.umur}\nDiagnosa: {self.diagnosa}")


rekam_medis1 = RekamMedis("Jamaludin", 35, "Flu")
rekam_medis1.info()
