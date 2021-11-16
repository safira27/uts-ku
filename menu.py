nama_minuman =[]
total=[]
tambah = None
keranjang=["pesanan selesai"]
def menu_minuman():
    print("===drink===")
    print("==============")
    print("pilihan menu :")
    print("==============")
    print("1. es teh")
    print("2. nutrisari")
    print("3. milk tea")
    print("4. es tebu")
    opsi = input("pilihan menunya :",)
    if opsi == "1":
        opsi= int(input("jumlah :"))
        print("kamu memesan",opsi)
        keranjang. append(nama_minuman)
    elif opsi == 2:
        opsi= int(input("jumlah :"))
        print("kamu mememesan :",opsi)
        keranjang. append(nama_minuman)
    if opsi == 3:
        opsi= int(input("jumlah :"))
        print("pesananmu :",opsi)
        keranjang. append(nama_minuman)
    elif opsi == 4:
        opsi= int(input("jumlah :"))
        print("pesananmu :",opsi)
        keranjang. append(nama_minuman)
    else:
        print("terimakasih")

def selesai():
    for pesanan in keranjang:
        print(pesanan) 

tambah = ""
while tambah !=( 'y' or 't' ):
    tambah = input("pesan lagi ?y/t :")
    if tambah == 'y':
        nama_minuman+= 0
        if tambah == 't':
            break
        else:
            break
    continue

menu_minuman()
         
