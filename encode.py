# Nicolas Postel

menu_option = 0
encode_str = ""


def encode(password):
    encoded = ""
    for digit in password:
        encoded += str(int(digit) + 3)
    return encoded

def decoder(password):


while menu_option != 3:
    print("Menu\n------------\n1. Encoder\n2. Decoder\n3. Quit")
    menu_option = int(input("Please enter an option: "))
    if menu_option == 1:
        encode_str = input("Please enter your password to encode: ")
        print("Your password has been encoded and stored!\n")
    elif menu_option == 2:
        print(f"The encoded password is {encode(encode_str)}, and the original password is {encode_str}.")
print()
