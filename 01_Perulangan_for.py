for i in range(1, 7):
    print("Bilangan :,", i)

# NPM berakhiran 30
x = 3
y = 0

# Bagian A: Urutan naik
print("Bagian A: Urutan naik")
for i in range(1, 12 + x + 1):
    print(i, end=", ")
print()

# Bagian B: Kelipatan 3
print("\nBagian B: Kelipatan 3")
for i in range(1, 5 + y + 1):
    print(3 * i, end=", ")
print()

# Bagian C: Urutan mundur
print("\nBagian C: Urutan mundur")
for i in range(12 + x, 0, -1):
    print(i, end=", ")
print()