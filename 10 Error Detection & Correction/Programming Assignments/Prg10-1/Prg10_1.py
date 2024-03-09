def crc_sender(dataword, divisor):
    k = len(dataword)
    n = len(divisor) + k - 1
    
    #Augmenting dataword with zeros
    augmented_dataword = dataword + '0' * (len(divisor) - 1)
    
    #Perform division
    remainder = polynomial_division(augmented_dataword, divisor)
    
    #Generating codeword by appending remainder to dataword
    codeword = dataword + remainder

    return codeword

def polynomial_division(dividend, divisor):
    #Perform Polynomial division
    remainder = list(dividend)
    divisor_length = len(divisor)
    current = 0
    
    while '1' in remainder[:len(remainder) - divisor_length + 1]:
        for i in range(divisor_length):
            remainder[current + i] = str(int(remainder[current + i]) ^ int(divisor[i]))
            
        while current < len(remainder) and remainder[current] == '0':
            current += 1
            
    return ''.join(remainder[-divisor_length + 1:])

def crc_receiver(codeword, divisor):
    k = len(codeword) - len(divisor) + 1
    
    #Performing division on received codeword
    syndrome = polynomial_division(codeword, divisor)
    
    #If syndrome is all zeros , accept dataword
    if all(bit == '0' for bit in syndrome):
        #Extracting original data by removing redundant bits
        dataword = codeword[:k]
        return True, dataword
    else:
        return False, None

def main():
    #Take input:
    # dataword = "1001" 
    # divisor = "1011"
    print("-----Sender Side------")
    dataword = input("Enter dataword: ")
    divisor = input("Enter divisor: ")

    #Sender side
    codeword = crc_sender(dataword, divisor)
    print(f"Dataword: {dataword}")
    print(f"Codeword: {codeword}\n")
    
    #Receiver side
    print("-----Receiver Side-----")
    # received_codeword = "1001110"
    received_codeword = input("Enter received codeword: ")
    accept, extracted_data = crc_receiver(received_codeword, divisor)
    if accept:
        print(f"(+) Data Accepted")
        print(f"Codeword: {received_codeword}")
        print(f"Dataword: {extracted_data}")
    else:
        print(f"(-) Data Rejected")

if __name__ == "__main__":
    main()
