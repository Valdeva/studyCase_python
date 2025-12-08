kata = input(" ketikan sebuah kata/ kalimat: ")
huruf_dicari = input(" masukan huruf yang ingin dicari: ")

for huruf in kata:
    if huruf == huruf_dicari:
        print(f"huruf '{huruf_dicari}' ditemukan dalam kata/ kalimat.")
        break
else:
    print(f"huruf '{huruf_dicari}' tidak ditemukan dalam kata/ kalimat.")