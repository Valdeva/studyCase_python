from buku import buku
from anggota import anggota
from data_manager import DataManager

class perpustakaan:
    def __init__(self, nama, alamat, auto_save=True):
        """
        Inisialisasi perpustakaan
        
        Args:
            nama: Nama perpustakaan
            alamat: Alamat perpustakaan
            auto_save: Otomatis menyimpan data setelah setiap operasi
        """
        self.nama = nama
        self.alamat = alamat
        self.daftar_buku = {}  # {judul: objek_buku}
        self.daftar_anggota = {}  # {id_anggota: objek_anggota}
        self.peminjaman = {}  # {id_anggota: [list_judul_buku]}
        self.riwayat = []  # List untuk menyimpan riwayat peminjaman
        self.auto_save = auto_save
        self.data_manager = DataManager()
        
        # Muat data yang tersimpan jika ada
        if auto_save:
            self.data_manager.muat_semua(self)

    def tambah_buku(self, judul, pengarang, tahun_terbit, kategori="Umum", isbn=None):
        """Menambahkan buku baru ke perpustakaan"""
        if judul in self.daftar_buku:
            print(f"Buku '{judul}' sudah ada di perpustakaan.")
            return False
        buku_baru = buku(judul, pengarang, tahun_terbit, kategori, isbn)
        self.daftar_buku[judul] = buku_baru
        print(f"Buku '{judul}' oleh {pengarang} ({tahun_terbit}) telah ditambahkan.")
        
        if self.auto_save:
            self.data_manager.simpan_buku(self.daftar_buku)
        return True

    def tambah_anggota(self, nama, id_anggota, alamat, no_telp=None, email=None):
        """Menambahkan anggota baru ke perpustakaan"""
        if id_anggota in self.daftar_anggota:
            print(f"ID Anggota {id_anggota} sudah terdaftar.")
            return False
        anggota_baru = anggota(nama, id_anggota, alamat, no_telp, email)
        self.daftar_anggota[id_anggota] = anggota_baru
        self.peminjaman[id_anggota] = []
        print(f"Anggota {nama} (ID: {id_anggota}) telah ditambahkan.")
        
        if self.auto_save:
            self.data_manager.simpan_anggota(self.daftar_anggota)
            self.data_manager.simpan_peminjaman(self.peminjaman)
        return True

    def tampilkan_buku(self):
        """Menampilkan semua buku yang tersedia"""
        if not self.daftar_buku:
            print("Tidak ada buku di perpustakaan.")
            return
        print("\n=== Daftar Buku di Perpustakaan ===")
        for idx, (judul, obj_buku) in enumerate(self.daftar_buku.items(), 1):
            print(f"{idx}. {obj_buku.info_buku()}")

    def tampilkan_anggota(self):
        """Menampilkan semua anggota yang terdaftar"""
        if not self.daftar_anggota:
            print("Tidak ada anggota terdaftar.")
            return
        print("\n=== Daftar Anggota ===")
        for idx, (id_anggota, obj_anggota) in enumerate(self.daftar_anggota.items(), 1):
            print(f"{idx}. {obj_anggota.info_anggota()}")

    def pinjam_buku(self, id_anggota, judul):
        """Memproses peminjaman buku"""
        if id_anggota not in self.daftar_anggota:
            print(f"ID Anggota {id_anggota} tidak terdaftar.")
            return False
        
        if judul not in self.daftar_buku:
            print(f"Buku '{judul}' tidak tersedia di perpustakaan.")
            return False

        if id_anggota not in self.peminjaman:
            self.peminjaman[id_anggota] = []

        if judul in self.peminjaman[id_anggota]:
            print(f"Buku '{judul}' sudah dipinjam oleh anggota ini.")
            return False

        # Update status buku menjadi dipinjam
        self.daftar_buku[judul].set_dipinjam()
        
        self.peminjaman[id_anggota].append(judul)
        anggota_info = self.daftar_anggota[id_anggota]
        anggota_info.tambah_peminjaman()
        riwayat_entry = f"{anggota_info.nama} (ID: {id_anggota}) meminjam '{judul}'"
        self.riwayat.append(riwayat_entry)
        print(f"Buku '{judul}' berhasil dipinjam oleh {anggota_info.nama}.")
        
        if self.auto_save:
            self.data_manager.simpan_buku(self.daftar_buku)
            self.data_manager.simpan_anggota(self.daftar_anggota)
            self.data_manager.simpan_peminjaman(self.peminjaman)
            self.data_manager.simpan_riwayat(self.riwayat)
        return True

    def kembalikan_buku(self, id_anggota, judul):
        """Memproses pengembalian buku"""
        if id_anggota not in self.daftar_anggota:
            print(f"ID Anggota {id_anggota} tidak terdaftar.")
            return False

        if id_anggota not in self.peminjaman or judul not in self.peminjaman[id_anggota]:
            print(f"Buku '{judul}' tidak sedang dipinjam oleh anggota ini.")
            return False

        # Update status buku menjadi tersedia
        if judul in self.daftar_buku:
            self.daftar_buku[judul].set_tersedia()

        self.peminjaman[id_anggota].remove(judul)
        anggota_info = self.daftar_anggota[id_anggota]
        riwayat_entry = f"{anggota_info.nama} (ID: {id_anggota}) mengembalikan '{judul}'"
        self.riwayat.append(riwayat_entry)
        print(f"Buku '{judul}' berhasil dikembalikan oleh {anggota_info.nama}.")
        
        if self.auto_save:
            self.data_manager.simpan_buku(self.daftar_buku)
            self.data_manager.simpan_peminjaman(self.peminjaman)
            self.data_manager.simpan_riwayat(self.riwayat)
        return True

    def tampilkan_peminjaman(self, id_anggota=None):
        """Menampilkan daftar buku yang sedang dipinjam"""
        if id_anggota:
            if id_anggota not in self.daftar_anggota:
                print(f"ID Anggota {id_anggota} tidak terdaftar.")
                return
            anggota_info = self.daftar_anggota[id_anggota]
            if id_anggota in self.peminjaman and self.peminjaman[id_anggota]:
                print(f"\n=== Buku yang dipinjam oleh {anggota_info.nama} ===")
                for idx, judul in enumerate(self.peminjaman[id_anggota], 1):
                    print(f"{idx}. {judul}")
            else:
                print(f"{anggota_info.nama} tidak sedang meminjam buku.")
        else:
            print("\n=== Daftar Peminjaman ===")
            ada_peminjaman = False
            for id_angg, daftar_judul in self.peminjaman.items():
                if daftar_judul:
                    ada_peminjaman = True
                    anggota_info = self.daftar_anggota[id_angg]
                    print(f"\n{anggota_info.nama} (ID: {id_angg}):")
                    for idx, judul in enumerate(daftar_judul, 1):
                        print(f"  {idx}. {judul}")
            if not ada_peminjaman:
                print("Tidak ada buku yang sedang dipinjam.")

    def tampilkan_riwayat(self):
        """Menampilkan riwayat peminjaman dan pengembalian"""
        if not self.riwayat:
            print("Belum ada riwayat peminjaman.")
            return
        print("\n=== Riwayat Peminjaman dan Pengembalian ===")
        for idx, entry in enumerate(self.riwayat, 1):
            print(f"{idx}. {entry}")

    def simpan_data(self):
        """Menyimpan semua data ke file"""
        return self.data_manager.simpan_semua(self)

    def muat_data(self):
        """Memuat semua data dari file"""
        self.data_manager.muat_semua(self)