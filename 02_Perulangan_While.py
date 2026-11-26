# NPM berakhiran 30
npm_akhir = 30


x = npm_akhir % 10
angka = 1
jumlah_tampil = 0
angka_lewati = x + 2
angka_berhenti = x + 11

print("X =", x)
print("Angka dilewati:", angka_lewati)
print("Angka berhenti:", angka_berhenti)
print()

hasil = []


while True:
    
    if angka == angka_berhenti:
        break

   
    if angka == angka_lewati:
        angka += 1
        continue

    
    hasil.append(str(angka))
    jumlah_tampil += 1
    angka += 1

print(", ".join(hasil))
print()


print("Jumlah bilangan:", jumlah_tampil)
print("Program selesai.")