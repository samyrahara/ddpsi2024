pilihan = int(input("""Pilih nomor pilihan:
1. Menghitung luas persegi 
2. Menghitung luas lingkaran
3. Menghitung luas segitiga
"""))

match pilihan: 
    case 1:
        print("Menghitung luas persegi ")
        s = int(input("masukkan nilai sisi: "))
        luasPersegi = s * s
        print(f"luas persegi dengan sisi {s} adalah {luasPersegi}")
    case 2: 
        print("Menghitung luas lingkaran")
        pi = 3.14
        r = int(input("masukkan nilai jari-jari: "))
        luasLingkaran = pi * r ** 2
        print(f"Luas lingkaran dengan jari-jari {r} adalah {luasLingkaran}")
    case 3: 
        print("Menghitung luas segitiga")
        alas = int(input("masukkan nilai alas: "))
        tinggi = int(input("masukkan nilai tinggi: "))
        luasSegitiga= 1/2 * alas * tinggi 
        print(f"luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luasSegitiga}")
    case _:
            print("input tidak falid")