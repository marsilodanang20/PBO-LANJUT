try:
    pilihan = int(input('Masukkan angka: '))
    assert pilihan > 0 # Cek nilai
except AssertionError :
    print("Angka tidak boleh Nol atau negative")
except ValueError :
    print("Input harus angka")