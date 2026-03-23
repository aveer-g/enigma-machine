# Create a dictionary
cipher_atbash = {"a":"z", "b":"y", "c":"x", "d":"w", "e":"v", "f":"u", "g":"t", "h":"s", "i":"r", "j":"q", "k":"p", "l":"o", "m":"n", "n":"m", "o":"l", "p":"k", "q":"j", "r":"i", "s":"h", "t":"g", "u":"f", "v":"e", "w":"d", "x":"c", "y":"b", "z":"a",}

# Ask user what cipher they want to use
def choice():
    while True:
        choice = input("What cipher do you want to use? [A]tbash or [C]aesar?\n").strip().title()
        message = input("Enter a message you want to encrypt (please enter only letters, no special characters or numbers):\n").strip().lower()
        if choice == "A" and message.isalpha():
            atbash(message)
            break
        elif choice == "A" and not message.isalpha():
            print("Something went wrong")
            continue
        elif choice== "C":
            while True:
                # make a loop for asking user if they want to encrypt or decrypting
                caesar_choice = input("Do you want to [E]ncrypt or [D]ecrypt\n").strip().title()
                if caesar_choice == "E":
                    caesar_encrypt(message)
                    break
                elif caesar_choice == "D":
                    caesar_decrypt(message)
                    break
                else:
                    print("Please enter a valid answer")
                    continue
            break
        else:
            print("Please enter a valid answer")

# function for atbash 
def atbash(message):
    # Make list
    final_message = []
    for letter in message:
        if letter in cipher_atbash:
            final_message.append(cipher_atbash[letter])
    print("The final message is: \n")
    print("".join(map(str, final_message)))
    restart()

# Encrypting function for caesar
def caesar_encrypt(message):
    # Make list
    final_message = []
    for letter in message:
        if letter.isalpha():
            shifted_letter = chr(ord(letter) + 3)
            final_message.append(shifted_letter)
        else:
            final_message.append(letter)
    print("".join(map(str, final_message)))
    restart()

# Decryting function for caesar
def caesar_decrypt(message):
    # Make list
    final_message = []
    for letter in message:
        if letter.isalpha():
            shifted_letter = chr(ord(letter) - 3)
            final_message.append(shifted_letter)
        else:
            final_message.append(letter)
    print("".join(map(str, final_message)))
    restart()

# Ask user if they want to use the program again
def restart():
    while True:
        restart = input("Do you want to do another encryption or decryption? [Y]es or [N]o\n").strip().title()
        if restart == "Y":
            choice()
            break
        elif restart == "N":
            print("Goodbye") 
            break
        else:
            print("Please enter a valid answer")

# Tell user what cipher the program is using
print("Hello, and welcome to the Enigma machine. This machine is able to work with two ciphers")
choice()
