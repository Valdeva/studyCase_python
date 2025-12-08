number = int(input("Enter a number to check if it's 1 to 20 "))
for i in range(1, number + 1):
    if i % 2 == 0:
        print(f"{i} is genap")
    else:
        print(f"{i} is ganjil")