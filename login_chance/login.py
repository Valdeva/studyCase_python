username = input("Enter your username: ")
password = input("Enter your password: ")
chance = 3
while chance > 0:
    if username == "admin" and password == "password123":
        print("Login successful!")
        break
    else:
        chance -= 1
        if chance == 0:
            print("Login failed. No more chances left.")
        else:
            print(f"Login failed. You have {chance} chances left.")
            username = input("Enter your username: ")
            password = input("Enter your password: ")