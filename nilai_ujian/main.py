siswa = input("Masukkan nama siswa: ")
nilai_ujian = int(input("Masukkan nilai ujian (0-100): "))
if 90 <= nilai_ujian <= 100:
    print(f"{siswa} mendapat Grade: A")
elif 80 <= nilai_ujian < 90:
    print(f"{siswa} mendapat Grade: B")
elif 70 <= nilai_ujian < 80:
    print(f"{siswa} mendapat Grade: C")
elif 60 <= nilai_ujian < 70:
    print(f"{siswa} mendapat Grade: D")
else:
    print(f"{siswa} mendapat Grade: E")