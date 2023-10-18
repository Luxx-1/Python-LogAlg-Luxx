#Nama = LUXX
#Program Ke = 11

#CASE MENCARI BERAPAKAH SISA UANG IBU?

#INPUT
print("");
print("------------ SISA UANG IBU -------------")    #tulisan atas
berat_telur = int(input("Berat Telur [KG] = "))    #pertanyaan 1
harga_telur = int(input("Harga Telur = Rp "))    #pertanyaan 2
uang_transport = int(input("Uang Transport [satu kali naik] = Rp "))    #pertanyaan 3
jumlah_naik = int(input("Jumlah Ibu Naik = "))    #pertanyaan 4
uang_ibu = int(input("Uang yang dimiliki ibu = Rp "))    #pertanyaan 5

#PROCESS
transport = uang_transport*jumlah_naik    #proses mencari harga transport
totalharga_telur = harga_telur*berat_telur    #proses mencari harga telur total
uang_sisa = uang_ibu - totalharga_telur-transport    #proses mencari uang sisa

#OUTPUT
print("-----------------------------------------")
print("Harga Telur Rp",totalharga_telur,"+ Transport Rp",transport)    #menampilkan rincian pengeluaran
print("Total Pengeluaran ibu = Rp ",totalharga_telur+transport)    #menampilkan total pengeluaran
print("Uang sisa yang dimiliki ibu = Rp ",uang_sisa)    #menampilkan uang sisa
print("")


