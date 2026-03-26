# Create a dictionary that maps each letter to its reverse
cipher_atbash = {"a":"z", "b":"y", "c":"x", "d":"w", "e":"v", "f":"u", "g":"t", "h":"s", "i":"r", "j":"q", "k":"p", "l":"o", "m":"n", "n":"m", "o":"l", "p":"k", "q":"j", "r":"i", "s":"h", "t":"g", "u":"f", "v":"e", "w":"d", "x":"c", "y":"b", "z":"a",}

# Ask user what cipher they want to use
def choice():
    while True: # Loops forever until a valid answer
        choice = input("What cipher do you want to use? [A]tbash or [C]aesar?\n").strip().title()
        message = input("Enter a message you want to encrypt (please enter only letters, no special characters or numbers):\n").strip().lower() # strip remove extra space, title make every first letter cap
        if choice == "A" and message.isalpha(): # alpha checks if text only has letters
            atbash(message) # Call atbash function
            break # Exits loop
        elif choice == "A" and not message.isalpha(): # If atbash chosen but message no letter
            print("Something went wrong")
            continue # Restarts the loop
        elif choice== "C":
            while True:
                # make a loop for asking user if they want to encrypt or decrypting
                caesar_choice = input("Do you want to [E]ncrypt or [D]ecrypt\n").strip().title() # strip remove extra space, title make every first letter cap
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
def caesar_encrypt(message): # Define func, uses math to encrypt + decrypt 
    # Make list
    final_message = [] # Make empty list so doesnt get mixed
    for letter in message: # Loop through each letter
        if letter.isalpha(): # Checks if each letter is a letter no number
            shifted_letter = chr(ord(letter) + 3)  # CONVERT letter to number by adding 3 (how cipher works), ord turns letter into # and chr does opposite
            final_message.append(shifted_letter) # add newly shifted letter in list
        else: # if not letter 
            final_message.append(letter) # add unchanged letter 
    print("".join(map(str, final_message))) # prints final encrypted msg
    restart()

# Decryting function for caesar
def caesar_decrypt(message): # Define func
    # Make list
    final_message = [] # make empty list
    for letter in message: # Loop through eacg letter
        if letter.isalpha(): # Checks if each letter is a letter 
            shifted_letter = chr(ord(letter) - 3) # Converts letter to number by subtracting 3 to get original
            final_message.append(shifted_letter) # Add newly reversed letter to list
        else:
            final_message.append(letter) # Add unchanged letter
    print("".join(map(str, final_message))) # prints final decrypted msg
    restart()

# Ask user if they want to use the program again
def restart(): # Define restart
    while True: # Loops valid ans
        restart = input("Do you want to do another encryption or decryption? [Y]es or [N]o\n").strip().title() # ask user to continue, strip remove extra space, title make every first letter cap
        if restart == "Y":
            choice()
            break # restart loop
        elif restart == "N":
            print("Goodbye!") 
            break # exit loop
        else:
            print("Please enter a valid answer") # print error

# Tell user what cipher the program is using
print("Hello, and welcome to the Enigma Machine. This machine is able to work with two ciphers those being either Atbash or Ceaser!")
choice() # start program w/ choice
