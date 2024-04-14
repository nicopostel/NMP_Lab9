#zhipeng guo

def encode(password):
    empass = ""
    for char in password:
        digit = int(char)
        enco = (digit + 3) % 10
        empass += str(enco)
    return empass

def decode(password):
    decoded = ''
    for digit in password:
        decoded += str(int(digit) - 3)
    return decoded

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        choice = input("Please enter an option: ")

        if choice == "1":
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == "2":
            encoded_password = input("Please enter the encoded password: ")
            decoded_password = decode(encoded_password)
            print("The encoded password is {}, and the original password is {}.".format(encoded_password,
                                                                                        decoded_password))
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
