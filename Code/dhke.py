import sympy

def dhke(P,G,a,b):
    x = pow(G,a,P)
    y = pow(G,b,P)
    ka = pow(y,a,P)
    kb = pow(x,b,P)
    print("Value of P is "+ str(P))
    print("Value of G is "+ str(G))
    print("Value of x is "+ str(x))
    print("Value of y is "+ str(y))
    print("Value of a is "+ str(a))
    print("Value of b is "+ str(b))
    print("Value of ka is "+ str(ka))
    print("Value of kb is "+ str(kb))

def dhkeDec(P,G,x=0,y=0):
    a = 1
    counter = 3
    while(counter):
        checkx = pow(G,a,P)
        if(checkx == x):
            print("decryption value is " + str(a))
            counter -= 1
        a += 1

if __name__ == "__main__":
    while(1):
        P = 0
        print("1.enc")
        print("2.dec")
        pilih = input("pilih:")
        if(pilih == "1"):
            while(not sympy.isprime(P)):
                P = int(input("masukkan P:"))
                G = P+1
            while(G>P):
                G = int(input("masukkan G:"))
            a = int(input("masukkan a:"))
            b = int(input("masukkan b:"))
            dhke(P,G,a,b)
        elif(pilih == "2"):
             while(not sympy.isprime(P)):
                 P = int(input("masukkan P:"))
                 G = P+1
             while(G>P):
                 G = int(input("masukkan G:"))
             x = int(input("masukkan x:"))
             dhkeDec(P,G,x)
        else:
            print()
