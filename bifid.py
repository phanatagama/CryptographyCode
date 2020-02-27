import numpy as np

def table():
        global table
        table = [["a","b","c","d","e"],
                 ["f","g","h","i","j"],
                 ["k","l","m","n","o"],
                 ["p","q","r","s","t"],
                 ["u","v","w","x","y/z"]]


def f(l, ch):
    ret = ""
    for i,sub_list in enumerate(l):
        if ch in sub_list:
            ret = ((i+1),(sub_list.index(ch)+1))
            val = "" +  str(ret[0])
            val += "" + str(ret[1])
            return val

def encrypt(plain):
    try:
        assert plain.isalpha()
        plain = plain.lower()
        mixup = [1]*(len(plain)*2)
        cipher = ""
        for char in range(len(plain)):
            row = int((ord(plain[char]) - ord('a')) / 5) + 1
            col = ((ord(plain[char]) - ord('a')) % 5) + 1
            if plain[char] == 'z':
                row = 5
                col = 5
            mixup[char] = row
            mixup[char+len(plain)] = col

        for twoint in range(len(plain)):
            bar = (1+twoint)*2
            foo = mixup[bar-2]
            zap = mixup[bar-1]
            cipher += table[foo-1][zap-1]

        print(cipher)
    except:
        print("Error :( wkwk")

def decrypt(cipher):
    assert cipher.isalpha()
    cipher = cipher.lower()
    number = ""
    midnum = [1]*(len(cipher)*2)
    dect = ""

    for char in cipher:
        number += f(table, char)

    for i in range(len(cipher)):
        row = int(number[i])
        col = int(number[i+len(cipher)])
        dect += table[row-1][col-1]
    print(dect)


if __name__ == "__main__":
    table()
    print("1.enc")
    print("2.dec")
    pilih = input("pilih: ")
    value = input("value char: ")
    if pilih == "1":
        encrypt(value)
    elif pilih == "2":
        decrypt(value)
    else:
        print("why?")
