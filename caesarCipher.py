try:
    #Saya nggak bedain karena secara konsep sama
    plain = input("Plain/Cipher: ")
    shift = int(input("Shift: "))
    enc = ""
    plain = plain.upper()
    print(plain)
    for i in range(len(plain)):
        tmp = ord(plain[i]) + (shift%26)
        if(tmp > 90):
            enc += chr((tmp + 65) % 91)
        else:
            enc += chr(tmp)

    print(enc)
except:
    print("Wrong Input bro")
