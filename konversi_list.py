#Nama   : Dede Maulana
#NIM    : 20230040012
#Kelas  : TI23C

# 1. Konversi nilai ke Integer
def konversi_integer(teks):
    try:
        nilai_integer = int (teks)
        print(f"nilai integer adalah {nilai_integer}")
    except ValueError:
        print("kesalahan : integer tidak valid")
        
konversi_integer("123")
konversi_integer("ABC")


# 2. Akses lis indeks
def akses_elemen(dafar_list, indeks):
    try:
        hasil = dafar_list[indeks]
        print(f"elemen di indeks {indeks} adalah {hasil}")
    except IndexError:
        print("kelasahan : indeks di luar jangkauan")
        
list_saya = [1, 2, 3]
akses_elemen(list_saya, 1)
akses_elemen(list_saya, 5)