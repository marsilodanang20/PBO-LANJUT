def ambil_nilai(kamus, kunci):
    try:
        nilai = kamus[kunci]
        print("Nilai dari kunci", kunci, "adalah:", nilai)
    except KeyError:
        print("Eror: Kunci", kunci, "tidak ditemukan dalam kamus")
        
# Contoh Pemanggilan fungsi dengan kunci yang tidak ada
data = {'nama': 'Jhon', 'usia': 30, 'kota': 'Jakarta'}

kunci = input("Memasukan kunci [nama, usia, kota]:")
ambil_nilai(data, kunci)