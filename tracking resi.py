print(">>> PENGECEKAN RESI PAKET <<<")


NAMA = input("NAMA PENERIMA : ")
ALAMAT = input("ALAMAT PENERIMA : ")
RESI = input("NOMOR RESI : ")

teks = "\nNAMA PENERIMA: {}\nALAMAT PENERIMA: {}\nNOMOR RESI: {}\n---".format(NAMA,ALAMAT,RESI)

nama_file=input("Masukkan nama file yang disimpan : ")
f = open(nama_file,"w")
f.write(teks)
f.close()
print("Menampilkan data dari file")

nama_file=input("Masukkan Nama File : ")
try:
    f = open(nama_file)
    while True:
        baris = f.readline()
        if len(baris) == 0 :
            break
        print(baris)
    f.close()
except:
    print("File yang diminta tidak ada")