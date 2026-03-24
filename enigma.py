# Create a dictionary that maps each letter to its reverse
cipher_atbash = {"a":"z", "b":"y", "c":"x", "d":"w", "e":"v", "f":"u", "g":"t", "h":"s", "i":"r", "j":"q", "k":"p", "l":"o", "m":"n", "n":"m", "o":"l", "p":"k", "q":"j", "r":"i", "s":"h", "t":"g", "u":"f", "v":"e", "w":"d", "x":"c", "y":"b", "z":"a",}

# Ask user what cipher they want to use
def choice():
    while True: # Loops forever until a valid answer
        choice = input("What cipher do you want to use? [A]tbash or [C]aesar?\n").strip().title()
        message = input("Enter a message you want to encrypt (please enter only letters, no special characters or numbers):\n").strip().lower()
        if choice == "A" and message.isalpha(): # alpha checks if text only has letters
            atbash(message) # Call atbash function
            break # Exits loop
        elif choice == "A" and not message.isalpha(): # If atbash chosen but message no letter
            print("Something went wrong")
            continue # Restarts the loop
        elif choice== "C":
            while True:
                # make a loop for asking user if they want to encrypt or decrypting
                caesar_choice = input("Do you want to [E]ncrypt or [D]ecrypt\n").strip().title()
                if caesar_choice == "E": # If user chooses encrypt
                    caesar_encrypt(message) # Calls encrypt function
                    break # Exit inner loop
                elif caesar_choice == "D": # If user choose decrypt
                    caesar_decrypt(message) # Calls decrpyt function
                    break # Exit inner loop
                else:
                    print("Please enter a valid answer")
                    continue # restarts the loop since no valid answer given
            break
        else:
            print("Please enter a valid answer") # if invalid cipher choice 

# function for atbash 
def atbash(message): 
    # Make list
    final_message = [] # Empty list to store results
    for letter in message: # Loops through each letter in msg
        if letter in cipher_atbash:
            final_message.append(cipher_atbash[letter]) # add converted letter to msg
    print("The final message is: \n")
    print("".join(map(str, final_message))) # Joins list into string and prints result
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
print("Hello, and welcome to the Enigma Machine. This machine is able to work with two ciphers those being either Atbash or Ceaser!")
choice()
