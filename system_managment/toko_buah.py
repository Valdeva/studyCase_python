buah = {
    'apel': 5000,
    'jeruk': 7000,
    'pisang': 3000,
    'mangga': 10000
}

def tampilkan_menu():
    print("=== Toko Buah ===")
    print("1. lihat daftar buah")
    print("2. tambah buah")
    print("3. Hapus Buah")
    print("4. Keluar")

def tambah_buah():
    # perulangan jika inputan tidak valid
    while True:
        nama_buah = input("Masukkan nama buah: ").lower()

        # validasi isi dari inputan nama buah
        if not nama_buah.isalpha():
            print("Nama buah hanya boleh mengandung huruf.")
            continue # ulangi input
        elif nama_buah in buah:
            print(f"{nama_buah} sudah ada dalam daftar dengan harga Rp{buah[nama_buah]}.")
            continue # ulangi input
        
        # perulangan untuk input harga buah jika tidak valid
        while True:

        # validasi harga buah
            
            harga_input = input("Masukkan harga buah: ")
            if not harga_input.isdigit():
                print("Harga buah harus berupa angka.")
                continue # ulangi input 
            harga_buah = int(harga_input)

            if harga_buah <= 0:
                print("Harga buah harus berupa angka positif.")
                continue # ulangi input
            break # keluar dari perulangan harga buah 
        
        # menambahkan buah ke dalam dictionary
        buah[nama_buah] = harga_buah
        print(f"{nama_buah} dengan harga Rp{harga_buah} telah ditambahkan ke dalam daftar.")
        break # keluar dari perulangan nama buah
                
def hapus_buah():
    while True:
        nama_buah = input("Masukkan nama buah yang akan dihapus: ").lower()
        if nama_buah in buah:
            del buah[nama_buah]
            print(f"{nama_buah} telah dihapus dari daftar.")
        else:
            print(f"{nama_buah} tidak ditemukan dalam daftar.")
        break       

def lihat_daftar_buah():
    if not buah:
        print("Daftar buah kosong.")
    else:
        print("Daftar Buah:")
        for nama, harga in buah.items():
            print(f"{nama.capitalize()}: Rp{harga}")

while True:
    tampilkan_menu()
    pilihan = input("Pilih menu (1-4): ")

    if pilihan == '1':
        lihat_daftar_buah()
    elif pilihan == '2':
        tambah_buah()
    elif pilihan == '3':
        hapus_buah()
    elif pilihan == '4':
        print("Terima kasih telah menggunakan Toko Buah.")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu 1-4.")
          
 