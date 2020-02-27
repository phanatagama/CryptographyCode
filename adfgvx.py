import math

table = ["8","p","3","d","1","n",
         "l","t","4","o","a","h",
         "7","k","b","c","5","z",
         "j","u","6","w","g","m",
         "x","s","v","i","r","2",
         "9","e","y","0","f","q"]
jumble = "adfgvx"


def adfgvx(val):
    try:
        assert val.isalnum()
        encode = ""
        num = ""
        for char in val:
            row = table.index(char) // 6
            col = table.index(char) %6
            num += str(row) + str(col)
        for i in range(len(num)):
            tmp = int(num[i])
            encode += jumble[tmp]
        print(encode)
        return encode
    except:
        print("error occur, this is adfgvx bro")

def dec_adfgvx(val):
    row = ""
    col = ""
    number = ""
    dec  = ""
    for i in val:
        number += str(jumble.index(i))

    for i in range(len(number)//2):
        bar = (1+i)*2
        foo = int(number[bar-2])
        zap = int(number[bar-1])
        nilai = foo*6+zap
        dec += table[nilai]

    print(dec)

def column(key,userval):
    try:
        assert key.isalpha()
        key = key.lower()
        userval = userval.lower()
        col=len(key)
        userval=userval.replace(' ','')
        if((len(userval)%col)!=0):
            userval+="x"*(len(userval)%col)

        o=[]
        for i in key:
            o.append(i)

        h=[]
        for i in range(col):
            h.append(userval[i:len(userval):col])

        dic=dict(zip(o,h))
        so=sorted(dic.keys())
        print(''.join(dic[i]for i in so))
    except:
        print("Whoops, Wrong maneh. repeat char a?")

def decryptMessage(cipher,key):
    msg = ""
    k_indx = 0
    msg_indx = 0
    msg_len = float(len(cipher))
    msg_lst = list(cipher)
    col = len(key)
    row = int(math.ceil(msg_len / col))
    key_lst = sorted(list(key))
    dec_cipher = []
    for _ in range(row):
        dec_cipher += [[None] * col]
    for _ in range(col):
        curr_idx = key.index(key_lst[k_indx])
        for j in range(row):
            dec_cipher[j][curr_idx] = msg_lst[msg_indx]
            msg_indx += 1
        k_indx += 1
    try:
        msg = ''.join(sum(dec_cipher, []))
    except TypeError:
        raise TypeError("Tidak boleh ada huruf yang sama")
    null_count = msg.count('_')
    if null_count > 0:
        return msg[: -null_count]
    print(msg)
    return(msg)


def tahapan(key,val):
    column(key,adfgvx(val))

def tahapan_dec(key,val):
    dec_adfgvx(decryptMessage(val,key))

if __name__ == "__main__":
    print("1.enc")
    print("2.dec")
    pilih = input("pilih: ")
    key = input("key: ")
    val = input("val: ")

    if(pilih == "1"):
        tahapan(key,val)
    elif(pilih == "2"):
        tahapan_dec(key,val)
    else:
        print("WOI")
