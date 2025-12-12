class buku:
    def __init__(self, judul, pengarang, tahun_terbit):
        self.judul = judul
        self.pengarang = pengarang
        self.tahun_terbit = tahun_terbit

    def info_buku(self):
        return f"{self.judul} oleh {self.pengarang}, diterbitkan pada {self.tahun_terbit}"