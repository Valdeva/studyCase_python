class anggota:
    def __init__(self, nama, id_anggota, alamat):
        self.nama = nama
        self.id_anggota = id_anggota
        self.alamat = alamat

    def info_anggota(self):
        return f"Anggota: {self.nama}, ID: {self.id_anggota}, Alamat: {self.alamat}"