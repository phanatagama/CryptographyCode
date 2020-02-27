import math

def check(key):
    key = key.lower()
    char = "abcdefghijlkmnopqrstuvwxyz"
    for i in char:
        count = key.count(i)
        if count > 1:
            return False
    return True


def column(key,userval,counter,key2="tidak"):
    try:
        assert check(key)
        counter -= 1
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
        res = ''.join(dic[i]for i in so)
        print(counter)
        if(counter != 0):
            print(res)
            column(key2,res,counter)
        else:
            print(res)
            return(res)
    except:
        print("you repeat your char?")

def decrypt2kali(cipher,key,key2):
    return decryptMessage(decryptMessage(cipher,key2),key)

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


if __name__ == "__main__":
    print("1.enc")
    print("2.dec")
    pilih = input("pilih: ")
    key = input("key: ")
    key2 = input("key2: ")
    val = input("val: ")
    if(pilih == "1"):
        column(key,val,2,key2)
    elif(pilih == "2"):
        decrypt2kali(val,key,key2)
    else:
        print("pilih bro")
