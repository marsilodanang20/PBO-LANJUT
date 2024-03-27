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
    alas_atas = minta_input("Masukkan panjang alas atas trapesium (cm): ")
    alas_bawah = minta_input("Masukkan panjang alas bawah trapesium (cm): ")
    tinggi = minta_input("Masukkan tinggi trapesium (cm): ")
    sisi_kanan = minta_input("Masukkan panjang sisi sejajar kanan trapesium (cm): ")
    sisi_kiri = minta_input("Masukkan panjang sisi sejajar kiri trapesium (cm): ")

    luas = (alas_atas + alas_bawah) * tinggi / 2
    keliling = alas_atas + alas_bawah + sisi_kanan + sisi_kiri

    print(f"Luas trapesium dengan alas atas {alas_atas} cm, alas bawah {alas_bawah} cm, dan tinggi {tinggi} cm adalah {luas} cm^2.")
    print(f"Keliling trapesium dengan alas atas {alas_atas} cm, alas bawah {alas_bawah} cm, sisi kanan {sisi_kanan} cm, dan sisi kiri {sisi_kiri} cm adalah {keliling} cm.")
except TypeError:
    print("Input tidak valid.")
