def encode_to_sb(text: str) -> str:
    b = text.encode('utf-8')
    #here, we have a bytes object
    #when we iterate it, it will return several integers(0-255)
    
    bits = "".join(f'{byte:08b}' for byte in b)
    #get the result
    
    return bits.replace("0", "s").replace("1", "b")

print(encode_to_sb(input("Please input the plaintext:")))