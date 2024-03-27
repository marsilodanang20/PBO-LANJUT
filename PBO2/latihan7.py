def hitung_balok():
    try:
        panjang = float(input("Masukkan panjang balok: "))
        lebar = float(input("Masukkan lebar balok: "))
        tinggi = float(input("Masukkan tinggi balok: "))
        
        assert panjang > 0 and lebar > 0 and tinggi > 0
        
        volume = panjang * lebar * tinggi
        luas_permukaan = 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))
        
        print("Volume Balok:", volume)
        print("Luas Permukaan Balok:", luas_permukaan)
    except ValueError:
        print("Error: Masukkan harus berupa angka")
    except AssertionError:
        print("Error: Panjang, lebar, dan tinggi balok harus lebih besar dari nol negative")


hitung_balok()
