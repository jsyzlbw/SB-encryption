def decode_from_sb(text: str) ->str:
    
    #remove all invalid chars
    filtered = "".join(ch for ch in text if ch in ("s", "b"))

    bits = filtered.replace("s", "0").replace("b", "1")
    
    if len(bits) % 8 != 0:
        raise ValueError("The ciphertext is  incomplete.")
    
    bytes_list = []
    for i in range(0, len(bits), 8):
        bytes_list.append(int(bits[i: i + 8], 2)) 
    
    return bytes(bytes_list).decode('utf-8')

print(decode_from_sb(input("Please input the ciphertext:")))