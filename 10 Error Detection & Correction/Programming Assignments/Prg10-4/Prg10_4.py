def calculate_checksum(data):
    L,R=0,1
    
    for byte in data:
        R = (R + byte) % 65521
        L = (L + R) % 65521
    checksum = (L << 16) + R
    return checksum

def sender_side(data):
    checksum = calculate_checksum(data)
    print("-----Sender Side-----")
    print(f"Data: {data}")
    print(f"Checksum: {checksum}\n")
    
    return checksum

def receiver_side(received_data, received_checksum):
    calculated_checksum = calculate_checksum(received_data)
    print("-----Receiver Side-----")
    print(f"Received Data: {received_data}")
    print(f"Received Checksum: {received_checksum}")
    print(f"Calculated Checksum: {calculated_checksum}")
    
    if calculated_checksum == received_checksum:
        print("Data Accepted")
    else:
        print("Data Rejected")
        
def main():
    data = [0x01, 0x02, 0x03, 0x04, 0x05]
    
    #Sender Side
    sent_checksum = sender_side(data)
    
    #Receiver Side
    #Assume the data and checksum are transmitted
    received_data = [0x01, 0x02, 0x03, 0x04, 0x05]
    receiver_side(received_data, sent_checksum)

if __name__ == "__main__":
    main()
