n = int(input("Masukan Nomor: "))

loop = 1
print("Tek kotek kotek kotek,anak ayam turun berkotek")
while n >=(loop+1):
    nA = n-1
    print("anak ayam tinggal lah",n,"mati satu tinggal",nA)
    while n == (loop+1):
        print("anak ayam tinggal lah 1 mati satu tinggal induknya")
        n = n-1
    n = n -1
    loop = loop 
while n == 1:
    print("anak ayam tinggal lah 1 mati satu tinggal induknya")
    n = n -1
    