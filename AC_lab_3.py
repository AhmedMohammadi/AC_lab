# Simplified-DES

def keyGeneration(key): # Define keyGeneration function

    P10 = [3,5,2,7,4,10,1,9,8,6] # P10 (permutate)
    P8 = [6,3,7,4,8,5,10,9] # P8 (select and permutate)
    keys = [] # Store the keys (K1, K2)
    
    p10 = "".join([key[P10[i]-1] for i in range(len(P10))]) # Kp10

    ls1 = p10[1:5]+p10[0]+p10[6:10]+p10[5] # LS1
    k1 = "".join([ls1[P8[i]-1] for i in range(len(P8))]) # Kp8(1)
    keys.append(k1) # Append to list "Keys"

    ls2 = ls1[2:5]+ls1[0:2]+ls1[7:10]+ls1[5:7] # LS2
    k2 = "".join([ls2[P8[i]-1] for i in range(len(P8))]) # Kp8(2)
    keys.append(k2) # Append to list "Keys"

    return keys # Return list "Keys"

def functionK(input, key): # Define functionK (Fk)

    P4 = [2,4,3,1] # P4 (permutate)
    EP = [4,1,2,3,2,3,4,1] # EP (expand and permutate)
    S0 = [ 
        ["01","00","11","10"], # S0 matrix
        ["11","10","01","00"],
        ["00","10","01","11"],
        ["11","01","11","10"],
    ]
    S1 = [
        ["00","01","10","11"], # S1 matrix
        ["10","00","01","11"],
        ["11","00","01","00"],
        ["10","01","00","11"],
    ]
    L4 = "".join(input[0:4]) # 4 left bits
    R4 = "".join(input[4:8]) # 4 right bits

    ep = [R4[EP[i]-1] for i in range(len(EP))] # Perform EP

    xor1 = [str(int(key[i]) ^ int(ep[i])) for i in range(len(key))] # XOR(1)

    # S0
    rowS0 = xor1[0:4:3]
    columnS0 = xor1[1:3] 
    s0 = S0[int("".join(rowS0),2)][int("".join(columnS0),2)]

    # S1
    rowS1 = xor1[4:8:3]
    columnS1 = xor1[5:7]
    s1 = S1[int("".join(rowS1),2)][int("".join(columnS1),2)]

    join = s0 + s1 # Join results of S0 and S1

    p4 = [join[P4[i]-1] for i in range(len(P4))] # Perform P4

    xor2 = "".join([str(int(p4[i]) ^ int(L4[i])) for i in range(len(p4))]) # XOR(2)
    xor2 += R4 # Join result of XOR(2) with 4 right bits

    return xor2 # Return XOR(2)
    
def simplifiedDES(plainText, key): # Define simplifiedDES function

    keys = keyGeneration(key) # Pass the input key to keyGeneration function
    k1, k2 = keys[0], keys[1] # Store the result of the function as K1 and K2
    
    IP = [6,1,3,4,2,8,7,5] # IP (initial permutation)
    ip = [plainText[IP[i]-1] for i in range(len(IP))] # Perform IP
    
    round_1 = functionK(ip,k1) # Round 1
    sw = round_1[4:8]+round_1[0:4] #SW (swap the halves)

    round_2 = functionK(sw, k2) # Round 2
    IIP = [2,5,3,4,8,1,7,6] # IP**−1 (inverse of IP)
    iip = "".join([round_2[IIP[i]-1] for i in range(len(IIP))]) # Perfrom IIP
    
    result = { # Store the results in dictionary
        "K1":k1,
        "K2":k2,
        "Encrypted Message": iip
    }
    return result # Return the results

def main(): # Define main function

    plainText, key = "11001111", "0011100110" # Inputs (Plain Text, key)
    result = simplifiedDES(plainText, key) # Pass the inputs (Plain Text, key) to simplifiedDES function
    print(f"Plain Text: {plainText}, Key: {key}") # Print the inputs (Plain Text, key)
    for value,key in result.items(): # Iterate through the results
        print(f"{value}: {key}") # Print the results

if __name__ == "__main__": # Call main function
    main()