from math import gcd # Import gcd from math library

def encryption(plain_text:str, a:int, b:int, alpha:list) -> list: # Defining encryption function
    encrypted_text = [] # Empty list to store encrypted text
    if gcd(a, 26) == 1: # Check if Key a is coprime with m
        for letter in plain_text: # Loop through plain text
            if letter == " ": # Check for space between words
                encrypted_text.append(" ") # Append space if true
            elif not letter.isalpha(): # Check for numbers
                encrypted_text.append(letter) # Append number if false
            else:
                index = alpha.index(letter) # Find the index of the letter in the alpha list
                result = (a * index + b) % 26 # Encryption formula
                encrypted_text.append(alpha[result]) # Append encrypted letter to encrypted_text list
    else:
        print("Invalid Input key 'a'")
        print("Key 'a' must be coprime with 'm'")
        exit() # Stop code execution
    return encrypted_text # Return encrypted_text list

def decryption(cipher_text:str, a:int, b:int, alpha:list) -> list: # Defining decryption function
    decrypted_text = [] # Empty list to store decrypted text
    for letter in cipher_text: # Loop through cipher text
        if letter == " ": # Check for space between word
            decrypted_text.append(" ") # Append space if true
        elif not letter.isalpha(): # Check for numbers
            decrypted_text.append(letter) # Append number if false
        else:
            for y in range(1, 26): # Loop between 1 and 25
                if (y * a % 26 == 1): # Check for the modular multiplicative inverse of a
                    index = alpha.index(letter) # Find the index of the letter in the alpha lis
                    result = y * (index - b) % 26 # Decryption formula
                    decrypted_text.append(alpha[result]) # Append decrypted letter to decrypted_text list
                    break # Stop the loop
    return decrypted_text

def main() -> None: # Defining main function

    alpha = [chr(i) for i in range(65,91)] # Alpha list to store the alphabets
    plain_text, a, b = "AFFINE CIPHER".upper(), 17, 20 # Inputs

    # Passing the inputs to the functions
    encrypted_text = encryption(plain_text = plain_text, a = a, b = b, alpha = alpha)
    decrypted_text = decryption(f"{"".join(encrypted_text)}", a = a, b = b, alpha = alpha)

    # Print the results of the functions
    print(f"Plain Text = {plain_text}, a = {a}, b = {b}")
    print(f"Encrypted Message: {"".join(encrypted_text)}")
    print(f"Decrypted Message: {"".join(decrypted_text)}")

# Calling the main fucntion
if __name__ == "__main__":
    main()