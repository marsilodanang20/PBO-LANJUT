class person:
    def __init__(self, nama, umur, alamat, no_telepon):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.no_telepon = no_telepon

class Dosen(person):
    def __init__(self, nama, umur, alamat, no_telepon, nidn, fakultas, prodi, jabatan_akademik, jabatan_struktural):
        super().__init__(nama, umur, alamat, no_telepon)
        self.nidn = nidn
        self.fakultas = fakultas
        self.prodi = prodi
        self.jabatan_akademik = jabatan_akademik
        self.jabatan_struktural = jabatan_struktural

class Mahasiswa(person):
    def __init__(self, nama, umur, alamat, no_telepon, nim, fakultas, prodi, angkatan):
        super().__init__(nama, umur, alamat, no_telepon)
        self.nim = nim
        self.fakultas = fakultas
        self.prodi = prodi
        self.angkatan = angkatan

class Staff(person):
    def __init__(self, nama, umur, alamat, no_telepon, departemen, jabatan):
        super().__init__(nama, umur, alamat, no_telepon)
        self.departemen = departemen
        self.jabatan = jabatan

class Satpam(person):
    def __init__(self, nama, umur, alamat, no_telepon, lokasi_jaga):
        super().__init__(nama, umur, alamat, no_telepon)
        self.lokasi_jaga = lokasi_jaga

class OB(person):
    def __init__(self, nama, umur, alamat, no_telepon, tugas):
        super().__init__(nama, umur, alamat, no_telepon)
        self.tugas = tugas

if __name__ == "__main__":
    dosen = Dosen("Prof. Dr. jamaludin", 45, "Jl. Tuparev No. 30", "089653512203", "22190", "Fakultas Teknik", "Teknik Informatika", "Guru Besar", "Ketua Program Studi")
    print("\nDosen:")
    print("Nama:", dosen.nama)
    print("Umur:", dosen.umur)
    print("Alamat:", dosen.alamat)
    print("No Telepon:", dosen.no_telepon)
    print("NIDN:", dosen.nidn)
    print("Fakultas:", dosen.fakultas)
    print("Program Studi:", dosen.prodi)
    print("Jabatan Akademik:", dosen.jabatan_akademik)
    print("Jabatan Struktural:", dosen.jabatan_struktural)

    mahasiswa = Mahasiswa("Danang", 20, "Jl. Pangeran sutajaya No. 5", "089653512203", "220511102", "Fakultas Teknik", "Teknik Informatika", 2023)
    print("\nMahasiswa:")
    print("Nama:", mahasiswa.nama)
    print("Umur:", mahasiswa.umur)
    print("Alamat:", mahasiswa.alamat)
    print("No Telepon:", mahasiswa.no_telepon)
    print("NIM:", mahasiswa.nim)
    print("Fakultas:", mahasiswa.fakultas)
    print("Program Studi:", mahasiswa.prodi)
    print("Angkatan:", mahasiswa.angkatan)

    staff = Staff("Budi", 30, "Jl. Karanggetas No. 8", "089653512203", "Keuangan", "Administrasi")
    print("\nStaff:")
    print("Nama:", staff.nama)
    print("Umur:", staff.umur)
    print("Alamat:", staff.alamat)
    print("No Telepon:", staff.no_telepon)
    print("Departemen:", staff.departemen)
    print("Jabatan:", staff.jabatan)

    satpam = Satpam("Jamal", 35, "Jl. Kalijaga No. 15", "089653512203", "Gedung Machdor")
    print("\nSatpam:")
    print("Nama:", satpam.nama)
    print("Umur:", satpam.umur)
    print("Alamat:", satpam.alamat)
    print("No Telepon:", satpam.no_telepon)
    print("Lokasi Jaga:", satpam.lokasi_jaga)

    ob = OB("Sarif", 25, "Jl. Pasuketan No. 20", "089653512203", "Kebersihan")
    print("\nOffice Boy:")
    print("Nama:", ob.nama)
    print("Umur:", ob.umur)
    print("Alamat:", ob.alamat)
    print("No Telepon:", ob.no_telepon)
    print("Tugas:", ob.tugas)
