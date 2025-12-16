import buah as buah_baru

def tampilkan_menu():
    print("=== Toko Buah OOP ===")
    print("1. Tampilkan Daftar Buah")
    print("2. Tambah Buah Baru")
    print("3. ubah harga Buah")
    print("4. ubah stok Buah")
    print("5. Hapus Buah")
    print("6. Keluar")


def tampilkan_daftar_buah():
    try:
        with open('buku.txt', 'r') as file:
            print("Daftar Buah Tersedia:")
            print("----------------------")
            for line in file:
                nama, harga, stok = line.strip().split(',')
                print(f"Nama: {nama}, Harga: {harga}, Stok: {stok}")
    except FileNotFoundError:   # error handling jika daftar buah kosong
        print("Daftar buah kosong.")   
    input("Press Enter to continue...")  # jeda sebelum input perulangan baru

def tambah_buah():
    while True:
        nama_buah = input("Masukkan nama buah: ")
        if not nama_buah.isalpha():  # input nama harus huruf
            print("Nama buah hanya boleh mengandung huruf.")
            continue
        harga_input = input("Masukkan harga buah: ")
        if not harga_input.isdigit():   #input harga harus angka
            print("Harga buah harus berupa angka.")
            continue
        stok_input = input("Masukkan stok buah: ")
        if not stok_input.isdigit():    # input stok harus angka
            print("Stok buah harus berupa angka.")
            continue

        nama = nama_buah
        harga = int(harga_input)
        stok = int(stok_input)

        if harga <= 0 or stok < 0:
            print("Harga harus positif dan stok tidak boleh negatif.")
            continue

        daftar_buah = buah_baru.Buah(nama, harga, stok)
        print(f"Buah {nama} dengan harga {harga} dan stok {stok} telah ditambahkan.")
        break
    input("Press Enter to continue...")  # jeda sebelum input perulangan baru

def hapus_buah():
    nama_buah = input("Masukkan nama buah yang akan dihapus: ")
    try:
        with open(buah_baru.txt, 'r') as file:
            lines = file.readlines()
            with open(buah_baru.txt, 'w') as file:
                found = False
                for line in lines:
                    nama, harga, stok = line.strip().split(',')
                    if nama.lower() != nama_buah.lower():
                        file.write(line)
                    else:
                        found = True
                if found:
                    print(f"Buah {nama_buah} telah dihapus dari daftar.")
                else:
                    print(f"Buah {nama_buah} tidak ditemukan dalam daftar.")
    except FileNotFoundError:
        print("Daftar buah kosong.")

        
while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == '1':
        tampilkan_daftar_buah()
    elif pilihan == '2':
        tambah_buah()
    elif pilihan == '3':
        print("Fitur ubah harga buah belum tersedia.")
        input("Press Enter to continue...")  # jeda sebelum input perulangan baru
    elif pilihan == '4':
        print("Fitur ubah stok buah belum tersedia.")
        input("Press Enter to continue...")  # jeda sebelum input perulangan baru
    elif pilihan == '5':
        print("Terima kasih telah menggunakan Toko Buah OOP.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        input("Press Enter to continue...")  # jeda sebelum input perulangan baru

tampilkan_menu()