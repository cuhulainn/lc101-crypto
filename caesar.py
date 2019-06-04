from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    encrypted = ""
    for char in text:
        encrypted += rotate_character(char, rot)
    return encrypted

def main():
    from sys import argv, exit
    
    
    if len(argv) == 2:
        if argv[1].isdigit():
            text = input("Type a message to encrypt:\n")
            rot = int(argv[1])
        else:
            print("usage: python caesar.py OR python caesar.py n")
            exit()
    elif len(argv) == 1:
        text = input("Type a message to encrypt:\n")
        rot = int(input("Rotate by:\n"))
    else:
        print("usage: python caesar.py OR python caesar.py n")
        exit()


    print(encrypt(text,rot))

if __name__ == "__main__":
    main()
