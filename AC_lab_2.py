# Task 1

letters = [chr(decimal) for decimal in range(65,91)]
numbers = [str(number) for number in range(len(letters))]
binary = [bin(ord(letter)).split("b")[1] for letter in letters]

for i in range(len(letters)):
    if i < 10:
        print(f"{numbers[i]}   |  {letters[i]}  |  {binary[i]}")
    else:
        print(f"{numbers[i]}  |  {letters[i]}  |  {binary[i]}")

######################################################################################################

# Task 2

def decryption(cipherText, key): # Defining decryption function
    plainText = "" # Store plain text
    for letter in range(len(cipherText)): # Iterate through the inputs
        if cipherText[letter] == " ": # Check for space
            plainText += cipherText[letter] # If true then ignore and add it
        else:
            cipherTextDecimal = ord(cipherText[letter]) - ord('a') # Convert the ascii character to it's english alphabet position
            keyDecimal = ord(key[letter % len(key)]) - ord('a') # Convert the ascii character to it's english alphabet position
            plainTextDecimal = (cipherTextDecimal - keyDecimal) % 26 # Change the alphabet position by subtracting it from the key
            plainText += chr(plainTextDecimal + ord('a')) # Convert to ascii character
    return plainText

def main(): # Defining main function
    cipherText, key = "bsaspp kkuosp", "rsidpy dkawoa" # Inputs
    decrypt = decryption(cipherText, key) # Pass the input to the decryption function
    print(f"Decrypted Message: {decrypt}") # Print the decrypted message

if __name__ == "__main__": # Call the main function
    main()

######################################################################################################

# Task 3

def dicCount(message): # Defining dictionary counter function

    dic = {} # Store the letter and it's frequency
    for letter in message: # Iterate through the message
        count = message.count(letter) # Count the frequency of each letter
        message = message.replace(letter, "") # Delete the letter when done
        if letter == " ": # Check for space
            continue # If true then ignore
        elif count == 0: # Check if count is zero
            continue # If true then ignore
        else:
            dic[letter] = count # Add the letter and it's frequency to the dictionary
    return dic # Return the dictionary

def dicSort(dic): # Defining dictionary sort function

    sorted = {} # Store the sorted letter and it's frequency
    whileCounter, forCounter = 0, 0  # Keep track of while/for loops
    maxValue, maxKey = 0, "" # Store maximum key/value

    while whileCounter != len(dic): # Keep the while loop running if whileCounter is smaller than the size of the dictionary
        for key, value in dic.items(): # Iterate through the dictionary
            if value > maxValue: # Check if value is bigger than maxValue
                maxKey = key
                maxValue = value
            forCounter += 1 # Increment forCounter by 1
            if forCounter == len(dic): # Check if forCounter equals the size of the dictionary
                sorted[maxKey] = maxValue # Add the sorted letter and it's frequency to the dictionary
                dic.update({maxKey:0}) # Change the maxKey to zero (Deletion)
                maxKey = "" # Delete maxKey
                maxValue = 0 # Delete maxValue
                forCounter = 0 # Delete forCounter
                whileCounter += 1 # Increment whileCounter by 1
    return sorted # Return the sorted dictionary

def main(): # Defining main function

    message = "SEIDPROHMRONEIA LEH CRVT FEIT NO SEPPTSOML ATT LEH ITGO ATAANEIA" # Input message
    count = dicCount(message) # Pass the message to dicCount function
    sorted = dicSort(count) # Pass the message to dicSorted function
    for key, value in sorted.items(): # To iterate through the dictionary
        print(key, value) # Print the key and value

if __name__ == "__main__": # Call the main function
    main()

######################################################################################################

# Task 4 (Bonus)

def xorCipher(message, key): # Defining XOR cipher function

    xorCipher = "" # Store the encrypted or decrypted message
    for letter in range(len(message)): # Iterate through the message and key
        if message[letter] == " ":
            xorCipher += message[letter]
        else:
            xorCipher += chr(ord(message[letter]) ^ ord(key[letter % len(key)])) # Convert the message/key to it's ascii decimal then perform the XOR operation and add it
    return xorCipher # Return the encrypted or decrypted message

def main(): # Defining main function

    plainText, key = "HELLO", "KEY" # Inputs
    encryption = xorCipher(plainText, key) # Pass the plain text and key to XOR cipher function for encryption
    decryption = xorCipher(encryption, key) # Pass the cipher text and key to XOR cipher function for decryption
    print(f"Encrypted Message: {encryption}") # Print the encrypted message
    print(f"Decrypted Message: {decryption}") # Print the decrypted message

if __name__ == "__main__": # Call the main function
    main()