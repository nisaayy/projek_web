print("===========Selamat Datang di Booking Online Hotel Jaya=============")
pembeli = input("Nama Pembeli : ")


# Definisikan jenis kamar dan harga per cabang
jenis_room = {
    1: "single room       ",
    2: "single bed        ",
    3: "suite room        ",
    4: "deluxe room       ",
    5: "presidential suite"
}

purwokerto_harga = {
    1: 250000,
    2: 250000,
    3: 500000,
    4: 750000,
    5: 1000000
}

purbalingga_harga = {
    1: 200000,
    2: 200000,
    3: 450000,
    4: 700000,
    5: 950000
}

jakarta_harga = {
    1: 500000,
    2: 500000,
    3: 750000,
    4: 900000,
    5: 1200000
}

bandung_harga = {
    1: 400000,
    2: 400000,
    3: 550000,
    4: 750000,
    5: 900000
}

yogyakarta_harga = {
    1: 250000,
    2: 250000,
    3: 400000,
    4: 600000,
    5: 750000
}

# Definisikan daerah cabang
daerah_cabang = {1: "Purwokerto", 2: "Purbalingga", 3: "Jakarta", 4: "Bandung", 5: "Yogyakarta"}

# Tampilkan daftar cabang hotel
print("======================= List Daerah Hotel =====================")
for i in daerah_cabang:
    print(" ", i, "", daerah_cabang[i])
# Pilih cabang dan jenis kamar
pilih_id = int(input("Pilih ID Hotel: "))

if pilih_id == 1:
    harga_kamar = purwokerto_harga
elif pilih_id == 2:
    harga_kamar = purbalingga_harga
elif pilih_id == 3:
    harga_kamar = jakarta_harga
elif pilih_id == 4:
    harga_kamar = bandung_harga
elif pilih_id == 5:
    harga_kamar = yogyakarta_harga
else:
    print("ID Hotel tidak valid")
    harga_kamar = None

if harga_kamar is not None:
    print("\nHarga kamar di ", daerah_cabang[pilih_id], ":")
    for room_id in harga_kamar:
        print(jenis_room[room_id], ": ", harga_kamar[room_id], " IDR")
    
    # Pilih jenis kamar dan waktu pesan
    pilih_jenis = int(input("Pilih ID jenis kamar: "))
    waktu_pesan = int(input("Masukkan jumlah hari pesan: "))
    
    if pilih_jenis in harga_kamar:
        kamar_harga = harga_kamar[pilih_jenis]
        if waktu_pesan > 1:
            bayar = waktu_pesan * kamar_harga
            print("\nTotal pembayaran untuk", waktu_pesan, "hari:", bayar, "IDR")
        else:
            print("Masukkan jumlah hari yang valid!")
    else:
        print("Jenis kamar tidak valid!")
else:
    print("Proses pembatalan, karena ID cabang tidak valid.")

print("transaksi  diatas Rp.500.000,- mendapatkan diskon 12%")
print("pembayaran only cash yaa..")
print("==============================================")
beli = input("Pilih Menu : ")
jumlah = int(input("Jumlah Pesenan : "))
bayar = jumlah * menu[harga_kamar]

if bayar > 100000:
    diskon = bayar * 12/100
    total = bayar - diskon
else:
    total = bayar


print("===================== DETAIL PEMBAYARAN ======================")
print("Menu yang dipesan        : " , beli)
print("Nama Pembeli             : " , pembeli)
print("Jumlah yang dipesan      : " , jumlah)
print("Total Biaya              : " , bayar)
print("total diskon             : " , diskon)
print("Total yang harus dibayar : " , total)
tunai = int(input("jumlah uang              : "))
kembali = tunai - total
print("jumlah uang              : " , tunai)
print("kembalian                : " , kembali)
print("terimakasih sudah berkunjung, semoga harimu menyenangkan")
 bhhjjjjjjjjjj
