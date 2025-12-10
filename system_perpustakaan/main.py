from perpustakaan import perpustakaan

def tampilkan_menu():
    """Menampilkan menu utama sistem perpustakaan"""
    print("\n" + "="*50)
    print("     SISTEM MANAJEMEN PERPUSTAKAAN")
    print("="*50)
    print("1. Tambah Buku")
    print("2. Tambah Anggota")
    print("3. Tampilkan Daftar Buku")
    print("4. Tampilkan Daftar Anggota")
    print("5. Pinjam Buku")
    print("6. Kembalikan Buku")
    print("7. Tampilkan Peminjaman")
    print("8. Tampilkan Riwayat")
    print("9. Info Perpustakaan")
    print("0. Keluar")
    print("="*50)

def main():
    """Fungsi utama untuk menjalankan sistem perpustakaan"""
    # Inisialisasi perpustakaan
    print("Selamat datang di Sistem Manajemen Perpustakaan!")
    nama_perpus = input("Masukkan nama perpustakaan: ").strip() or "Perpustakaan Umum"
    alamat_perpus = input("Masukkan alamat perpustakaan: ").strip() or "Jl. Perpustakaan No. 1"
    
    perpus = perpustakaan(nama_perpus, alamat_perpus)
    print(f"\nPerpustakaan '{perpus.nama}' di {perpus.alamat} telah dibuat!")

    while True:
        tampilkan_menu()
        pilihan = input("\nPilih menu (0-9): ").strip()

        if pilihan == "1":
            # Tambah Buku
            print("\n--- Tambah Buku Baru ---")
            judul = input("Masukkan judul buku: ").strip()
            if not judul:
                print("Judul buku tidak boleh kosong!")
                continue
            pengarang = input("Masukkan nama pengarang: ").strip() or "Tidak diketahui"
            tahun_terbit = input("Masukkan tahun terbit: ").strip()
            if not tahun_terbit.isdigit():
                print("Tahun terbit harus berupa angka!")
                continue
            kategori = input("Masukkan kategori buku (Enter untuk 'Umum'): ").strip() or "Umum"
            isbn = input("Masukkan ISBN (opsional, Enter untuk skip): ").strip() or None
            perpus.tambah_buku(judul, pengarang, int(tahun_terbit), kategori, isbn)

        elif pilihan == "2":
            # Tambah Anggota
            print("\n--- Tambah Anggota Baru ---")
            nama = input("Masukkan nama anggota: ").strip()
            if not nama:
                print("Nama anggota tidak boleh kosong!")
                continue
            id_anggota = input("Masukkan ID anggota: ").strip()
            if not id_anggota:
                print("ID anggota tidak boleh kosong!")
                continue
            alamat = input("Masukkan alamat anggota: ").strip() or "Tidak diketahui"
            no_telp = input("Masukkan nomor telepon (opsional, Enter untuk skip): ").strip() or None
            email = input("Masukkan email (opsional, Enter untuk skip): ").strip() or None
            perpus.tambah_anggota(nama, id_anggota, alamat, no_telp, email)

        elif pilihan == "3":
            # Tampilkan Daftar Buku
            perpus.tampilkan_buku()

        elif pilihan == "4":
            # Tampilkan Daftar Anggota
            perpus.tampilkan_anggota()

        elif pilihan == "5":
            # Pinjam Buku
            print("\n--- Pinjam Buku ---")
            perpus.tampilkan_anggota()
            id_anggota = input("\nMasukkan ID anggota: ").strip()
            if not id_anggota:
                print("ID anggota tidak boleh kosong!")
                continue
            perpus.tampilkan_buku()
            judul = input("\nMasukkan judul buku yang ingin dipinjam: ").strip()
            if not judul:
                print("Judul buku tidak boleh kosong!")
                continue
            perpus.pinjam_buku(id_anggota, judul)

        elif pilihan == "6":
            # Kembalikan Buku
            print("\n--- Kembalikan Buku ---")
            id_anggota = input("Masukkan ID anggota: ").strip()
            if not id_anggota:
                print("ID anggota tidak boleh kosong!")
                continue
            if id_anggota in perpus.peminjaman and perpus.peminjaman[id_anggota]:
                print(f"\nBuku yang sedang dipinjam:")
                for idx, judul in enumerate(perpus.peminjaman[id_anggota], 1):
                    print(f"{idx}. {judul}")
                judul = input("\nMasukkan judul buku yang ingin dikembalikan: ").strip()
                if not judul:
                    print("Judul buku tidak boleh kosong!")
                    continue
                perpus.kembalikan_buku(id_anggota, judul)
            else:
                print("Anggota ini tidak sedang meminjam buku.")

        elif pilihan == "7":
            # Tampilkan Peminjaman
            print("\n--- Daftar Peminjaman ---")
            pilih = input("Tampilkan semua (a) atau per anggota (s)? [a/s]: ").strip().lower()
            if pilih == "s":
                id_anggota = input("Masukkan ID anggota: ").strip()
                if id_anggota:
                    perpus.tampilkan_peminjaman(id_anggota)
                else:
                    print("ID anggota tidak boleh kosong!")
            else:
                perpus.tampilkan_peminjaman()

        elif pilihan == "8":
            # Tampilkan Riwayat
            perpus.tampilkan_riwayat()

        elif pilihan == "9":
            # Info Perpustakaan
            print("\n=== Informasi Perpustakaan ===")
            print(f"Nama: {perpus.nama}")
            print(f"Alamat: {perpus.alamat}")
            print(f"Total Buku: {len(perpus.daftar_buku)}")
            print(f"Total Anggota: {len(perpus.daftar_anggota)}")
            total_peminjaman = sum(len(daftar) for daftar in perpus.peminjaman.values())
            print(f"Buku yang Sedang Dipinjam: {total_peminjaman}")

        elif pilihan == "0":
            # Keluar
            print("\nMenyimpan data...")
            perpus.simpan_data()
            print("Data berhasil disimpan!")
            print("\nTerima kasih telah menggunakan Sistem Manajemen Perpustakaan!")
            print("Sampai jumpa!")
            break

        else:
            print("\nPilihan tidak valid! Silakan pilih menu 0-9.")

        # Pause sebelum menampilkan menu lagi
        input("\nTekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    main()

