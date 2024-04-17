class Person:
    def __init__(self, nama, umur, alamat, no_telepon):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat
        self.no_telepon = no_telepon

class Manager(Person):
    def __init__(self, nama, umur, alamat, no_telepon, divisi, idmanager):
        super().__init__(nama, umur, alamat, no_telepon)
        self.divisi = divisi
        self.idmanager = idmanager

class Programmer(Person):
    def __init__(self, nama, umur, alamat, no_telepon, posisi, id_programer):
        super().__init__(nama, umur, alamat, no_telepon)
        self.posisi = posisi
        self.idprogramer = id_programer

class Staff(Person):
    def __init__(self, nama, umur, alamat, no_telepon, jabatan, idmanager):
        super().__init__(nama, umur, alamat, no_telepon)
        self.jabatan = jabatan
        self.idmanager = idmanager

class Teknisi(Person):
    def __init__(self, nama, umur, alamat, no_telepon, divisi, idmanager):
        super().__init__(nama, umur, alamat, no_telepon)
        self.divisi = divisi
        self.idmanager = idmanager

if __name__ == "__main__":
    manager = Manager("Jamaludin", 20, "Jl. Tuparev No. 10", "089653512203", "keuangan", "22566")
    print("Manager:")
    print("Nama:", manager.nama)
    print("Umur:", manager.umur)
    print("Alamat:", manager.alamat)
    print("No Telepon:", manager.no_telepon)
    print("Divisi:", manager.divisi)
    print("ID Manager:", manager.idmanager)
    
    programmer = Programmer("Sarifuddin", 19, "Jl. Kalijaga No. 5", "089653512203", "Software Developer", "2677")
    print("\nProgrammer:")
    print("Nama:", programmer.nama)
    print("Umur:", programmer.umur)
    print("Alamat:", programmer.alamat)
    print("No Telepon:", programmer.no_telepon)
    print("Posisi:", programmer.posisi)
    print("ID Programmer:", programmer.idprogramer)

    staff = Staff("Angga", 19, "Jl. Pangeran Sutajaya No. 8", "089653512203", "HR Assistant", "54321")
    print("\nStaff:")
    print("Nama:", staff.nama)
    print("Umur:", staff.umur)
    print("Alamat:", staff.alamat)
    print("No Telepon:", staff.no_telepon)
    print("Jabatan:", staff.jabatan)
    print("ID Manager:", staff.idmanager)

    teknisi = Teknisi("Adit", 25, "Jl. Karanggetas No. 15", "089653512203", "Maintenance", "67890")
    print("\nTeknisi:")
    print("Nama:", teknisi.nama)
    print("Umur:", teknisi.umur)
    print("Alamat:", teknisi.alamat)
    print("No Telepon:", teknisi.no_telepon)
    print("Divisi:", teknisi.divisi)
    print("ID Manager:", teknisi.idmanager)
