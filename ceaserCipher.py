def encryption(plaintext, key):
    ans = ""
    for i in range(len(plaintext)):
        cha = plaintext[i]

        if cha.isupper():
            ans = ans + chr((ord(cha) + key - 65) % 26 + 65)
        elif cha.isdigit():
            ans = ans + str((int(cha) + key) % 10)
        elif cha == " ":
            ans = ans + " "
        elif cha.islower():
            ans = ans + chr((ord(cha) + key - 97) % 26 + 97)
        else:
            ans = ans + chr((ord(cha) + key) % 128)
    return ans


def decryption(encrypted_text, key):
    ans = ""

    for i in range(len(encrypted_text)):
        cha = encrypted_text[i]

        if cha.isupper():
            ans = ans + chr((ord(cha) - key - 65) % 26 + 65)
        elif cha.isdigit():
            ans = ans + str((int(cha) - key) % 10)
        elif cha == " ":
            ans = ans + " "
        elif cha.islower():
            ans = ans + chr((ord(cha) - key - 97) % 26 + 97)
        else:
            ans = ans + chr((ord(cha) - key) % 128)
    return ans


def display():
    while True:
        print("[1].encryption")
        print("[2].Decryption")
        print("[3].exit")
        print("Select the operation:")
        choice = int(input())

        if choice == 1:
            plaintext = input("enter your string:")
            key = int(input("enter key:"))

            print("\n*********************************************************")
            print("plain text:" + plaintext)
            print("cipher text is:" + encryption(plaintext, key))
            print("*********************************************************\n")


        elif choice == 2:
            encrypted_text = input("Enter the text to decrypt:")
            key = int(input("enter key:"))

            print("\n*********************************************************")
            print("cipher text:" + encrypted_text)
            print("plain text is:" + decryption(encrypted_text, key))
            print("*********************************************************\n")

        elif choice == 3:
            print("\n*********************************************************")
            print("exit from the code....")
            print("*********************************************************\n")
            break

        else:
            print("\n*********************************************************")
            print("invalid operation")
            print("*********************************************************\n")


display()
