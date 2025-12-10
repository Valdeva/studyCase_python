class buku:
    def __init__(self, judul, pengarang, tahun_terbit, kategori="Umum", isbn=None, status="Tersedia"):
        """
        Inisialisasi objek buku
        
        Args:
            judul: Judul buku
            pengarang: Nama pengarang
            tahun_terbit: Tahun terbit buku
            kategori: Kategori buku (default: "Umum")
            isbn: ISBN buku (opsional)
            status: Status buku - "Tersedia" atau "Dipinjam" (default: "Tersedia")
        """
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit
        self.kategori = kategori
        self.isbn = isbn
        self.status = status

    def info_buku(self):
        """Mengembalikan informasi lengkap buku dalam format string"""
        info = f"{self.judul} oleh {self.pengarang}, diterbitkan pada {self.tahun_terbit}"
        if self.kategori != "Umum":
            info += f", Kategori: {self.kategori}"
        if self.isbn:
            info += f", ISBN: {self.isbn}"
        info += f" - Status: {self.status}"
        return info

    def info_singkat(self):
        """Mengembalikan informasi singkat buku"""
        return f"{self.judul} oleh {self.pengarang} ({self.tahun_terbit})"

    def ubah_status(self, status_baru):
        """Mengubah status buku"""
        if status_baru in ["Tersedia", "Dipinjam"]:
            self.status = status_baru
            return True
        return False

    def set_dipinjam(self):
        """Mengatur status buku menjadi dipinjam"""
        self.status = "Dipinjam"

    def set_tersedia(self):
        """Mengatur status buku menjadi tersedia"""
        self.status = "Tersedia"

    def to_dict(self):
        """Mengkonversi objek buku ke dictionary untuk penyimpanan"""
        return {
            "judul": self.judul,
            "pengarang": self.pengarang,
            "tahun_terbit": self.tahun_terbit,
            "kategori": self.kategori,
            "isbn": self.isbn,
            "status": self.status
        }

    @classmethod
    def from_dict(cls, data):
        """Membuat objek buku dari dictionary"""
        return cls(
            judul=data.get("judul", ""),
            pengarang=data.get("pengarang", ""),
            tahun_terbit=data.get("tahun_terbit", ""),
            kategori=data.get("kategori", "Umum"),
            isbn=data.get("isbn"),
            status=data.get("status", "Tersedia")
        )