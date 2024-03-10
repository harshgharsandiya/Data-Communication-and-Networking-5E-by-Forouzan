def calculate_checksum(data):
    L,R = 0,0
    
    for byte in data:
        R = (R + byte) % 256
        L = (L + R) % 256
    checksum = (L << 8) + R
    return checksum

def sender_side(data):
    checksum = calculate_checksum(data)
    print("-----Sender Side-----")
    print(f"Data: {data}")
    print(f"Checksum: {checksum}\n")
    return checksum

def receiver_side(received_data, received_checksum):
    calculated_checksum = calculate_checksum(received_data)
    print("-----Reciever Side-----")
    print(f"Recived Data: {received_data}")
    print(f"Received Checksum: {received_checksum}")
    print(f"Calculated Checksum: {calculated_checksum}")
    if calculated_checksum == received_checksum:
        print("Data accepted")
    else:
        print("Data rejected")

def main():
    data = [0x01, 0x02, 0x03, 0x04, 0x05]
    
    #Sender Side
    sent_checksum = sender_side(data)
    
    #Assume the data and chechsum are transmitted
    received_data = [0x01, 0x02, 0x03, 0x04, 0x05]
    receiver_side(received_data, sent_checksum)
    
if __name__ == "__main__":
    main()
