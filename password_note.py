from crypt.fernet import Fernet

master_pwd = input("Master_password?\n>>>").lower()

def view():
    print("View your passwords...")

    with open("passwords.txt","r") as file:

        for line in file.readlines():
            print(line.strip())
        
            split = None
            s_opts = ["y","n"]
            while not split in s_opts:
                split = input("Would you like to split user_name and password?(y/n): ")
        
            if split == "y":
                user,pwd = line.strip().split("|")#split takes "" as argument
                print(f"user_name = {user}\npassword = {pwd}")
            else:
                print("No is accessed.")

def add():
    print("Add new passwords...")

    name = input("User_name >")
    new_pwd = input("Add a new_password > ")

    with open("passwords.txt","a") as file: #open

        file.write(f"{name}|{new_pwd}\n")

while True:

    options = ["view","add","q"]

    mode = None

    while not mode in options:

        mode = input("Select an option > view, add or q to quit?\n>>> ").lower()
    
    if mode == "q":
        print("Oops, see you later!")
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Unknown error occured!")
    
    

    