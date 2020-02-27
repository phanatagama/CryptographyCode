def encrypt(words,plain,key):
    try:
        assert len(key) == len(plain)
        assert words.isalpha() or plain.isalpha() or key.isalpha()
        plain = plain.lower()
        key = key.lower()
        words = words.lower()
        insert = words + "abcdefghiklmnopqrstuvwxyz"
        table = []
        num = ""
        for i in range(len(insert)):
            if(insert[i] not in table):
                table.append(insert[i])
        for i in range(len(plain)):
            row = (table.index(plain[i])//5)+1
            col = (table.index(plain[i])%5)+1
            row2 = (table.index(key[i])//5)+1
            col2 = (table.index(key[i])%5)+1
            num = int(str(row) + str(col))
            num2 = int(str(row2) + str(col2))
            res = num +num2
            print(res,end ="-", sep='')
        print()
    except:
        print("Opps, Somethin Went Wrong")

def decrypt(words,cipher,key):
    cipher_list = cipher.split("-")
    table = []
    num = ""
    insert = words + "abcdefghiklmnopqrstuvwxyz"
    for i in range(len(insert)):
        if(insert[i] not in table):
            table.append(insert[i])

    for i in range(len(key)):
        row2 = (table.index(key[i])//5)+1
        col2 = (table.index(key[i])%5)+1
        cipher_list[i] = int(cipher_list[i]) - int(str(row2) + str(col2))


    dec  = ""

    for i in range(len(cipher_list)):
        foo = int(cipher_list[i]//10)-1
        bar = int(cipher_list[i]%10)-1
        nilai = foo*5+bar
        dec += table[nilai]
    print(dec)



if __name__ == "__main__":
    print("1.enc")
    print("2.dec")
    pilih = input("pilih: ")
    words = input("words: ")
    plain = input("input: ")
    key = input("key: ")
    if(pilih == "1"):
        encrypt(words,plain,key)
    elif(pilih == "2"):
        decrypt(words,plain,key)
    else:
        print("Pilih cuy")
