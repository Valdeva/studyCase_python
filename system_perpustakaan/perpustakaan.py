class perpustakaan:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat
        self.buku = {}

    def tambah_buku(self, judul, pengarang):
        self.buku[judul] = pengarang
        print(f"Buku '{judul}' oleh {pengarang} telah ditambahkan.")

    def tampilkan_buku(self):
        if not self.buku:
            print("Tidak ada buku di perpustakaan.")
            return
        print("Daftar Buku di Perpustakaan:")
        for judul, pengarang in self.buku.items():
            print(f"- '{judul}' oleh {pengarang}")