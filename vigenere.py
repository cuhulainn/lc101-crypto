from helpers import alphabet_position, rotate_character

def encrypt(text, key):
    encrypted = ""
    key_loc = 0
    for char in text:
        if char.isalpha():
          rot = alphabet_position(key[key_loc])
          key_loc += 1
          key_loc = key_loc % len(key)
          encrypted += rotate_character(char, rot)
        else:
          encrypted += char
    return encrypted

def main():
    from sys import argv, exit

    if len(argv) == 2:
        if argv[1].isalpha():
            text = input("Type a message to encrypt:\n")
            key = argv[1]
        else:
            print("usage: \npython vigenere.py \nOR \npython vigenere.py key\n\nArguments:\n-key : The string to be used as a ""key"" to encrypt your message. \nShould only contain alphabetic characters-- no numbers or special characters. \nCan also be input after running the program.")
            exit()
    
    elif len(argv) == 1:
        text = input("Type a message to encrypt:\n")
        key = (input("Encryption key:\n"))
    
    else:
        print("usage: python vigenere.py \nOR \npython vigenere.py key\n\nArguments:\n-key : The string to be used as a ""key"" to encrypt your message. \nShould only contain alphabetic characters-- no numbers or special characters. \nCan also be input after running the program.")
        exit()    

    print(encrypt(text, key))

if __name__ == "__main__":
    main()