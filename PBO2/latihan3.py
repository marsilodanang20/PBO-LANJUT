while True:
    try:
        input_angka1 = float(input("Masukkan angka pembilang: "))
        input_angka2 = float(input("Masukkan angka penyebut: "))
        hasil_pembagian = input_angka1 / input_angka2
        break
    except ValueError:
        print("Error: Masukkan harus berupa angka!")
    except ZeroDivisionError:
        print("Error: Tidak bisa melakukan pembagian dengan angka nol!")

print("Hasil pembagian:", hasil_pembagian)