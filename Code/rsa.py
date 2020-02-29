number_to_encrypt = 512

p = 67
q = 83
e = 59

n = p*q
phi_n = (p-1)*(q-1)

e = 59
def is_coprime_phi(phi_n, coprime_to_check):
    while phi_n % coprime_to_check == 0:
        coprime_to_check = input("Enter a prime number, to check if coprime with phi_n")
        e = coprime_to_check
    return True

if not is_coprime_phi(phi_n,e):
    raise ValueError("e is not coprime with phi_n")

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(coprime, phi_n):
    g, x, y = egcd(coprime, phi_n)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % phi_n

d = modinv(e,phi_n)

pub_k = [e,n]

priv_k = [d,n]

def encrypt_this(m):
    result = pow(m,e,n)
    return result

def decrypt_this(c):
    plain = pow(c,d,n)
    return plain


enc = encrypt_this(number_to_encrypt)
print("Encypted number: ",enc)

dec = decrypt_this(enc)
print("Decrypted plain number: ",dec)
