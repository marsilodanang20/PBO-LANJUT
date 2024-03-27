def hitung_trapesium():
    try:
        alas_atas = float(input("Masukkan panjang alas atas trapesium: "))
        alas_bawah = float(input("Masukkan panjang alas bawah trapesium: "))
        tinggi = float(input("Masukkan tinggi trapesium: "))
        
        assert alas_atas > 0 and alas_bawah > 0 and tinggi > 0
        
        luas = 0.5 * (alas_atas + alas_bawah) * tinggi
        sisi_miring = ((alas_bawah - alas_atas) ** 2 + tinggi ** 2) ** 0.5
        keliling = alas_atas + alas_bawah + (2 * sisi_miring)
        
        print("Luas Trapesium:", luas)
        print("Keliling Trapesium:", keliling)
    except ValueError:
        print("Error: Masukkan harus berupa angka")
    except AssertionError:
        print("Error: Panjang alas dan tinggi harus lebih besar dari nol atau negative")


hitung_trapesium()
