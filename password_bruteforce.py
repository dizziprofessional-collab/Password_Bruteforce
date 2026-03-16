real_password = "1n3vitabl3"
with open("100k-most-used-passwords-NCSC.txt", "r", encoding = "utf-8", errors ="ignore") as file:
    for password in file:
        password = password.strip()
        
        print("Trying", password)

        if password == real_password:
            print("Right.")
            break
        else: print("Wrong.")


