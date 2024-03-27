def minta_input(pesan):
    while True:
        try:
            nilai_input = input(pesan)
            if nilai_input.strip() == "":
                raise ValueError("Input tidak boleh kosong")
            nilai_numerik = float(nilai_input)
            if nilai_numerik <= 0:
                raise ValueError("Nilai harus lebih besar dari 0")
            return nilai_numerik 
        except ValueError as e:
            print(e)

try:
    panjang = minta_input("Masukkan panjang balok (cm): ")
    lebar = minta_input("Masukkan lebar balok (cm): ")
    tinggi = minta_input("Masukkan tinggi balok (cm): ")

    volume = panjang * lebar * tinggi
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)

    print(f"Volume balok dengan panjang {panjang} cm, lebar {lebar} cm, dan tinggi {tinggi} cm adalah {volume} cm^3.")
    print(f"Luas permukaan balok dengan panjang {panjang} cm, lebar {lebar} cm, dan tinggi {tinggi} cm adalah {luas_permukaan} cm^2.")
except TypeError:
    print("Input tidak valid.")
