class Buah:
   
    def __init__(self, nama, harga, stok):
        with open('buku.txt', 'a') as file:
            file.write(f"{nama},{harga},{stok}\n")
        self.nama = nama
        self.harga = harga
        self.stok = stok


        