#Small Prgram to review writing/reading files and functions in python 
Mpwd = input("What is the Master password? ")

def view():
    # First argument is file name 
    # Second argument is mode. 'r' is read mode, 'w' is overwrite and write mode, 'a' add something to the END or create a new file
    with open("passwords.txt", 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print(f"User: {user} | Password: {passw}")

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", 'a') as f:
        f.write(name + "|" + pwd + "\n")



while True:
    mode = input("Would you like to add a new password or view existing ones (view, Or add). Press 'q' to Quit ")
    if mode == 'q':
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else: 
        print("Invalid mode. ")
        continue