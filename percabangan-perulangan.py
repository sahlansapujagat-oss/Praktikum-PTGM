# Kalkulator sederhana dengan percabangan dan perulangan

while True:
    print("\n=== Kalkulator Sederhana ===")
    print("1. Penjumlahan (+)")
    print("2. Pengurangan (-)")
    print("3. Perkalian (×)")
    print("4. Pembagian (÷)")
    print("5. Keluar")

    pilihan = input("Pilih operasi (1-5): ")

    if pilihan == '5':
        print("Terima kasih telah menggunakan kalkulator!")
        break  # keluar dari perulangan

    # Meminta input angka dari pengguna
    try:
        angka1 = float(input("Masukkan angka pertama: "))
        angka2 = float(input("Masukkan angka kedua: "))
    except ValueError:
        print("Input tidak valid! Harus berupa angka.")
        continue  # kembali ke awal loop

    # Percabangan untuk menentukan operasi
    if pilihan == '1':
        hasil = angka1 + angka2
        print(f"Hasil: {angka1} + {angka2} = {hasil}")
    elif pilihan == '2':
        hasil = angka1 - angka2
        print(f"Hasil: {angka1} - {angka2} = {hasil}")
    elif pilihan == '3':
        hasil = angka1 * angka2
        print(f"Hasil: {angka1} × {angka2} = {hasil}")
    elif pilihan == '4':
        if angka2 != 0:
            hasil = angka1 / angka2
            print(f"Hasil: {angka1} ÷ {angka2} = {hasil}")
        else:
            print("Error: Pembagian dengan nol tidak diperbolehkan!")
    else:
        print("Pilihan tidak valid! Silakan coba lagi.")