def hitung_jajar_genjang():
    try:
        alas = float(input("Masukkan panjang alas jajar genjang: "))
        tinggi = float(input("Masukkan tinggi jajar genjang: "))
        sisi_miring = float(input("Masukkan panjang sisi miring jajar genjang: "))
        
        assert alas > 0 and tinggi > 0 and sisi_miring > 0
        
        luas = alas * tinggi
        keliling = 2 * (alas + sisi_miring)
        
        print("Luas Jajar Genjang:", luas)
        print("Keliling Jajar Genjang:", keliling)
    except ValueError:
        print("Error: Masukkan harus berupa angka")
    except AssertionError:
        print("Error: Panjang alas, tinggi, dan sisi miring harus lebih besar dari nol atau negative")


hitung_jajar_genjang()
