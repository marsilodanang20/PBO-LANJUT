while True:
    try:
        input_angka1 = float(input("Masukkan angka pertama: "))
        input_angka2 = float(input("Masukkan angka kedua: "))
        hasil_penjumlahan = input_angka1 + input_angka2
        break 
    except ValueError:
        print("Error: Masukkan harus berupa angka!")

print("Hasil penjumlahan:", hasil_penjumlahan)
