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
    alas = minta_input("Masukkan panjang alas jajar genjang (cm): ")
    tinggi = minta_input("Masukkan tinggi jajar genjang (cm): ")
    sisi_miring = minta_input("Masukkan panjang sisi miring jajar genjang (cm): ")

    luas = alas * tinggi
    keliling = 2 * (alas + sisi_miring)

    print(f"Luas jajar genjang dengan alas {alas} cm dan tinggi {tinggi} cm adalah {luas} cm^2.")
    print(f"Keliling jajar genjang dengan alas {alas} cm dan panjang sisi miring {sisi_miring} cm adalah {keliling} cm.")
except TypeError:
    print("Input tidak valid.")
