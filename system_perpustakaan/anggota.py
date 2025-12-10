from datetime import datetime

class anggota:
    def __init__(self, nama, id_anggota, alamat, no_telp=None, email=None, tanggal_daftar=None):
        """
        Inisialisasi objek anggota
        
        Args:
            nama: Nama anggota
            id_anggota: ID unik anggota
            alamat: Alamat anggota
            no_telp: Nomor telepon (opsional)
            email: Email anggota (opsional)
            tanggal_daftar: Tanggal pendaftaran (default: tanggal hari ini)
        """
        self.nama = nama
        self.id_anggota = id_anggota
        self.alamat = alamat
        self.no_telp = no_telp
        self.email = email
        self.tanggal_daftar = tanggal_daftar or datetime.now().strftime("%Y-%m-%d")
        self.status = "Aktif"  # Aktif, Nonaktif, Diblokir
        self.total_peminjaman = 0  # Total buku yang pernah dipinjam

    def info_anggota(self):
        """Mengembalikan informasi lengkap anggota dalam format string"""
        info = f"Anggota: {self.nama}, ID: {self.id_anggota}, Alamat: {self.alamat}"
        if self.no_telp:
            info += f", Telp: {self.no_telp}"
        if self.email:
            info += f", Email: {self.email}"
        info += f", Status: {self.status}, Terdaftar: {self.tanggal_daftar}"
        return info

    def info_singkat(self):
        """Mengembalikan informasi singkat anggota"""
        return f"{self.nama} (ID: {self.id_anggota})"

    def ubah_status(self, status_baru):
        """Mengubah status anggota"""
        if status_baru in ["Aktif", "Nonaktif", "Diblokir"]:
            self.status = status_baru
            return True
        return False

    def tambah_peminjaman(self):
        """Menambah counter total peminjaman"""
        self.total_peminjaman += 1

    def update_kontak(self, no_telp=None, email=None):
        """Memperbarui informasi kontak anggota"""
        if no_telp:
            self.no_telp = no_telp
        if email:
            self.email = email

    def to_dict(self):
        """Mengkonversi objek anggota ke dictionary untuk penyimpanan"""
        return {
            "nama": self.nama,
            "id_anggota": self.id_anggota,
            "alamat": self.alamat,
            "no_telp": self.no_telp,
            "email": self.email,
            "tanggal_daftar": self.tanggal_daftar,
            "status": self.status,
            "total_peminjaman": self.total_peminjaman
        }

    @classmethod
    def from_dict(cls, data):
        """Membuat objek anggota dari dictionary"""
        return cls(
            nama=data.get("nama", ""),
            id_anggota=data.get("id_anggota", ""),
            alamat=data.get("alamat", ""),
            no_telp=data.get("no_telp"),
            email=data.get("email"),
            tanggal_daftar=data.get("tanggal_daftar")
        )