def main():
    # byts
    b = bytes([0x41, 0x42,0x43,0x44])
    print(b)
    s = "This is a string"
    print(s)
    
    # decode bytes to string
    s2 = b.decode('utf-8')
    
    print(s + s2)
    
    # encode string to byts
    b2 = s.encode('utf-8')
    print(b2 + b)
    
    # text encoded into byts
    b3 = s.encode('utf-32')
    print(b3)
if __name__ == "__main__":
    main()