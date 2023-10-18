#Nama = LUXX
#Program Ke = 11

#CASE MENENTUKAN HARGA PEMBELI

#INPUT
print("--------- HARGA MANGGA -----------")
hrg = int(input("Harga Per KG = Rp "))
brt = int(input("Berat Pembelian [KG] = "))

#PROCESS
harga_total = brt*hrg

#OUTPUT
print("-----------------------------------")
print("Harga Yang Harus Dibayar = Rp ",harga_total)