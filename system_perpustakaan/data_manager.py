import json
import os
from datetime import datetime
from buku import buku
from anggota import anggota

class DataManager:
    """Kelas untuk mengelola penyimpanan dan pembacaan data perpustakaan"""
    
    def __init__(self, folder_data="data"):
        """
        Inisialisasi DataManager
        
        Args:
            folder_data: Nama folder untuk menyimpan data
        """
        self.folder_data = folder_data
        self.file_buku = os.path.join(folder_data, "buku.txt")
        self.file_anggota = os.path.join(folder_data, "anggota.txt")
        self.file_riwayat = os.path.join(folder_data, "riwayat.txt")
        self.file_peminjaman = os.path.join(folder_data, "peminjaman.txt")
        
        # Pastikan folder data ada
        if not os.path.exists(folder_data):
            os.makedirs(folder_data)

    def simpan_buku(self, daftar_buku):
        """
        Menyimpan daftar buku ke file
        
        Args:
            daftar_buku: Dictionary dengan key judul dan value objek buku
        """
        try:
            data = {}
            for judul, obj_buku in daftar_buku.items():
                data[judul] = obj_buku.to_dict()
            
            with open(self.file_buku, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error menyimpan data buku: {e}")
            return False

    def baca_buku(self):
        """
        Membaca daftar buku dari file
        
        Returns:
            Dictionary dengan key judul dan value objek buku
        """
        daftar_buku = {}
        if not os.path.exists(self.file_buku):
            return daftar_buku
        
        try:
            with open(self.file_buku, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for judul, buku_data in data.items():
                daftar_buku[judul] = buku.from_dict(buku_data)
            
            return daftar_buku
        except Exception as e:
            print(f"Error membaca data buku: {e}")
            return daftar_buku

    def simpan_anggota(self, daftar_anggota):
        """
        Menyimpan daftar anggota ke file
        
        Args:
            daftar_anggota: Dictionary dengan key id_anggota dan value objek anggota
        """
        try:
            data = {}
            for id_anggota, obj_anggota in daftar_anggota.items():
                data[id_anggota] = obj_anggota.to_dict()
            
            with open(self.file_anggota, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error menyimpan data anggota: {e}")
            return False

    def baca_anggota(self):
        """
        Membaca daftar anggota dari file
        
        Returns:
            Dictionary dengan key id_anggota dan value objek anggota
        """
        daftar_anggota = {}
        if not os.path.exists(self.file_anggota):
            return daftar_anggota
        
        try:
            with open(self.file_anggota, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for id_anggota, anggota_data in data.items():
                daftar_anggota[id_anggota] = anggota.from_dict(anggota_data)
            
            return daftar_anggota
        except Exception as e:
            print(f"Error membaca data anggota: {e}")
            return daftar_anggota

    def simpan_riwayat(self, riwayat):
        """
        Menyimpan riwayat peminjaman ke file
        
        Args:
            riwayat: List string riwayat peminjaman (semua riwayat)
        """
        try:
            # Format: setiap entry dengan timestamp
            data_riwayat = []
            for entry in riwayat:
                # Jika entry sudah berupa dict dengan timestamp, gunakan langsung
                if isinstance(entry, dict):
                    data_riwayat.append(entry)
                else:
                    # Jika entry berupa string, tambahkan timestamp
                    data_riwayat.append({
                        "waktu": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        "aktivitas": entry
                    })
            
            with open(self.file_riwayat, 'w', encoding='utf-8') as f:
                json.dump(data_riwayat, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error menyimpan riwayat: {e}")
            return False

    def baca_riwayat(self):
        """
        Membaca riwayat peminjaman dari file
        
        Returns:
            List string riwayat peminjaman
        """
        riwayat = []
        if not os.path.exists(self.file_riwayat):
            return riwayat
        
        try:
            with open(self.file_riwayat, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            for entry in data:
                if isinstance(entry, dict):
                    riwayat.append(f"[{entry.get('waktu', '')}] {entry.get('aktivitas', '')}")
                else:
                    riwayat.append(entry)
            
            return riwayat
        except Exception as e:
            print(f"Error membaca riwayat: {e}")
            return riwayat

    def simpan_peminjaman(self, peminjaman):
        """
        Menyimpan data peminjaman ke file
        
        Args:
            peminjaman: Dictionary dengan key id_anggota dan value list judul buku
        """
        try:
            with open(self.file_peminjaman, 'w', encoding='utf-8') as f:
                json.dump(peminjaman, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error menyimpan data peminjaman: {e}")
            return False

    def baca_peminjaman(self):
        """
        Membaca data peminjaman dari file
        
        Returns:
            Dictionary dengan key id_anggota dan value list judul buku
        """
        peminjaman = {}
        if not os.path.exists(self.file_peminjaman):
            return peminjaman
        
        try:
            with open(self.file_peminjaman, 'r', encoding='utf-8') as f:
                peminjaman = json.load(f)
            
            return peminjaman
        except Exception as e:
            print(f"Error membaca data peminjaman: {e}")
            return peminjaman

    def simpan_semua(self, perpus):
        """
        Menyimpan semua data perpustakaan
        
        Args:
            perpus: Objek perpustakaan
        """
        hasil = True
        hasil &= self.simpan_buku(perpus.daftar_buku)
        hasil &= self.simpan_anggota(perpus.daftar_anggota)
        hasil &= self.simpan_peminjaman(perpus.peminjaman)
        hasil &= self.simpan_riwayat(perpus.riwayat)
        return hasil

    def muat_semua(self, perpus):
        """
        Memuat semua data perpustakaan dari file
        
        Args:
            perpus: Objek perpustakaan
        """
        perpus.daftar_buku = self.baca_buku()
        perpus.daftar_anggota = self.baca_anggota()
        perpus.peminjaman = self.baca_peminjaman()
        perpus.riwayat = self.baca_riwayat()
        
        # Inisialisasi peminjaman untuk anggota yang belum ada
        for id_anggota in perpus.daftar_anggota:
            if id_anggota not in perpus.peminjaman:
                perpus.peminjaman[id_anggota] = []

