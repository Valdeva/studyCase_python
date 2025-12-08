item = int(input("Masukkan jumlah item yang dibeli: "))
total_harga = 0
for i in range(item):
    nama_item = input(f"Masukkan nama item ke-{i+1}: ")
    harga_item = float(input(f"Masukkan harga {nama_item}: "))
    print(f"Item: {nama_item}, Harga: {harga_item}")
    total_harga += harga_item
    print(f"Total harga sementara: {total_harga}")
if total_harga > 100000:
    diskon = total_harga * 0.1
    total_harga_setelah_diskon = total_harga - diskon
    print(f"Anda mendapatkan diskon 10%! Total harga setelah diskon: {total_harga_setelah_diskon}")
elif total_harga > 50000:
    diskon = total_harga * 0.05
    total_harga_setelah_diskon = total_harga - diskon
    print(f"Anda mendapatkan diskon 5%! Total harga setelah diskon: {total_harga_setelah_diskon}")