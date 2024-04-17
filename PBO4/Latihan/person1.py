class person:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

class Dokter(person):
    def __init__(self, nama, umur, alamat, spesialisasi, nomor_Lisensi):
        super().__init__(nama, umur, alamat)
        self.spesialisasi = spesialisasi
        self.nomor_Lisensi = nomor_Lisensi

class Perawat(person):
    def __init__(self, nama, umur, alamat, bidang, nomor_registrasi):
        super().__init__(nama, umur, alamat)
        self.bidang = bidang
        self.nomor_registrasi = nomor_registrasi

class Karyawan(person):
    def __init__(self, nama, umur, alamat, departemen, nomor_pegawai):
        super().__init__(nama, umur, alamat)
        self.departemen = departemen
        self.nomor_pegawai = nomor_pegawai

if __name__ == "__main__":
    dokter = Dokter("dr. Danang ", 22, "Jl. Pangeran Sutajaya No. 10", "Spesialis Gigi", "20900")
    print("\nDokter:")
    print("Nama:", dokter.nama)
    print("Umur:", dokter.umur)
    print("Alamat:", dokter.alamat)
    print("Spesialisasi:", dokter.spesialisasi)
    print("Nomor Lisensi:", dokter.nomor_Lisensi)

    perawat = Perawat("Suster Vina", 28, "Jl. Karaggetas No. 5", "IGD", "45229")
    print("\nPerawat:")
    print("Nama:", perawat.nama)
    print("Umur:", perawat.umur)
    print("Alamat:", perawat.alamat)
    print("Bidang:", perawat.bidang)
    print("Nomor Registrasi:", perawat.nomor_registrasi)

    karyawan = Karyawan("Jamal", 26, "Jl. Kalijaga No. 8", "Administrasi", "45889")
    print("\nKaryawan:")
    print("Nama:", karyawan.nama)
    print("Umur:", karyawan.umur)
    print("Alamat:", karyawan.alamat)
    print("Departemen:", karyawan.departemen)
    print("Nomor Pegawai:", karyawan.nomor_pegawai)
