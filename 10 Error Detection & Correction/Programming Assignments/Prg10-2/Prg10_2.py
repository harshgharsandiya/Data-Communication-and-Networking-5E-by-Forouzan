def calculate_checksum(dataword):
    #Calculate sum from data unit
    checksum = sum(int(data, 2) for data in dataword)
    
    #convert checksum to binary
    checksum = bin(checksum)[2:]
    
    #Find Checksum
    a = checksum[-len(dataword[0]):]
    b = checksum[:-len(dataword[0])]
    checksum = bin(int(a,2) + int(b,2))[2:]
    
    return checksum

def add_checksum(dataword):
    checksum = calculate_checksum(dataword)
    return dataword + [checksum]

def verify_checksum(codeword):
    checksum = calculate_checksum(codeword[:-1])
    if (checksum == codeword[-1]):
        return True
    else:
        return False

def main():
    #Sender Side
    print("-----Sender Side------")
    dataword = ['0111', '1011', '1100', '0000', '0110']
    codeword = add_checksum(dataword)
    print(f"Dataword: {(dataword)}")
    print(f"Codeword: {codeword}\n")
    
    #Receiver Side
    print("-----Receiver Side-----")
    received_codeword = ['0111', '1011', '1100', '0000', '0110', '110']
    accept = verify_checksum(received_codeword)
    if accept:
        print("(+) Dataword Accepted")
        print(f"Codeword: {received_codeword}")
        print(f"Dataword: {received_codeword[:-1]} ")
    else:
        print("(-) Dataword rejected")
    

if __name__ == "__main__":
    main()
