# Mini sistem rental kendaraan (NPM berakhiran 30)
npm_akhir = 30

# 1. Siapkan x dan z sesuai NPM, total_sewa = 0, jumlah_transaksi = 0
x = npm_akhir % 10          # digit terakhir
z = npm_akhir // 10 % 10    # digit kedua dari belakang
total_sewa = 0
jumlah_transaksi = 0
persen_diskon = 5 + x
batas_diskon = 300000 + z * 1000

print("x =", x)
print("z =", z)
print("Persen diskon:", persen_diskon, "%")
print("Batas diskon: Rp", batas_diskon)
print()
print("=== DAFTAR KENDARAAN ===")
print("1. Sepeda       - Rp 20000/hari")
print("2. Motor Matic  - Rp 75000/hari")
print("3. Motor Sport  - Rp 100000/hari")
print("4. Mobil        - Rp 300000/hari")
print("0. Selesai")

# 2. Terima pilihan kendaraan
while True:
    print()
    pilihan = int(input("Pilih kendaraan (0-4): "))

    if pilihan == 0:
        break

    if pilihan == 1:
        harga = 20000
    elif pilihan == 2:
        harga = 75000
    elif pilihan == 3:
        harga = 100000
    elif pilihan == 4:
        harga = 300000
    else:
        print("Pilihan tidak valid!")
        continue

    # 3. Masukkan lama sewa (hari)
    lama_sewa = int(input("Lama sewa (hari): "))
    if lama_sewa < 1:
        print("Lama sewa minimal 1 hari!")
        continue

    subtotal = harga * lama_sewa
    total_sewa += subtotal
    jumlah_transaksi += 1
    print("Subtotal: Rp", subtotal)

# 4. Hitung diskon setelah keluar dari while
if total_sewa >= batas_diskon:
    diskon = total_sewa * persen_diskon // 100
else:
    diskon = 0
total_bayar = total_sewa - diskon

# 5. Tampilkan hasil
print()
print("=== RINGKASAN ===")
print("Jumlah transaksi:", jumlah_transaksi)
print("Total sebelum diskon: Rp", total_sewa)
print("Diskon: Rp", diskon)
print("Total bayar: Rp", total_bayar)
print("Program selesai.")