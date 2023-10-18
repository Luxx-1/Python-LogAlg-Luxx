#NAMA = LUXX (ABDEE)
#NIM = 19231060
#PROGRAM KE = 15
#CASE = MENCARI BILANGAN TERBESAR

#INPUT
bil_a = int(input("Bilangan Pertama = "))
bil_b = int(input("Bilangan Kedua = "))
bil_c = int(input("Bilangan Ketiga = "))
bil_d = int(input("Bilangan Keempat = "))

#PENCARIAN MENGGUNAKAN MAX
#bil_max = (max(bil_a,bil_b,bil_c,bil_d))
#print ("Bilangan Terbesar Adalah = ",bil_max)

#PENCARIAN MENGGUNAKAN IF
if bil_a>bil_b and bil_a>bil_c and bil_a>bil_d:
    print ("")
    print ("Bilangan Terbesar Adalah Bilangan Pertama: ",bil_a)
    
if bil_b>bil_a and bil_b>bil_c and bil_b>bil_d:
    print ("")
    print ("Bilangan Terbesar Adalah Bilangan Kedua: ",bil_b)
    
if bil_c>bil_a and bil_c>bil_b and bil_c>bil_d:
    print ("")
    print ("Bilangan Terbesar Adalah Bilangan Ketiga: ",bil_c)
    
if bil_d>bil_a and bil_d>bil_b and bil_d>bil_c:
    print ("")
    print ("Bilangan Terbesar Adalah Bilangan Keempat: ",bil_d)