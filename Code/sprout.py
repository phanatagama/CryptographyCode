key         = [False]*80
iv          = [False]*70
nfsr        = [False]*40
lfsr        = [False]*41
keystream   = [False]*420
input_lfsr  = False
input_nfsr  = False
temp_g_nfsr = [False]*15
temp_h      = [False]*5
g = z = h = B = k = False
biner       = [False]*7
c4_arr      = [False]*420
c4          = False

t = 0

input_8     = [False]*8
encrypt_8   = [False]*8
decrypt_8   = [False]*8
input_12    = [False]*12
encrypt_12  = [False]*12
decrypt_12  = [False]*12
input_16    = [False]*16
encrypt_16  = [False]*16
decrypt_16  = [False]*16

def feedback_lfsr_kg():
    input_lfsr = lfsr[40] ^ lfsr[35] ^ lfsr[25] ^ lfsr[20] ^ lfsr[15] ^ lfsr[6] ^ True

def feedback_nfsr_kg():
    temp_g_nfsr[0] = nfsr[0]
    temp_g_nfsr[1] = nfsr[13]
    temp_g_nfsr[2] = nfsr[19]
    temp_g_nfsr[3] = nfsr[35]
    temp_g_nfsr[4] = nfsr[39]
    temp_g_nfsr[5] = (nfsr[2] and nfsr[25])
    temp_g_nfsr[6] = (nfsr[3] and nfsr[5])
    temp_g_nfsr[7] = (nfsr[7] and nfsr[8])
    temp_g_nfsr[8] = (nfsr[14] and nfsr[21])
    temp_g_nfsr[9] = (nfsr[16] and nfsr[18])
    temp_g_nfsr[10] = (nfsr[22] and nfsr[24])
    temp_g_nfsr[11] = (nfsr[26] and nfsr[32])
    temp_g_nfsr[12] = (nfsr[33] and nfsr[36] and nfsr[37] and nfsr[38])
    temp_g_nfsr[13] = (nfsr[10] and nfsr[11] and nfsr[12])
    temp_g_nfsr[14] = (nfsr[27] and nfsr[30] and nfsr[31])
    g = temp_g_nfsr[0] ^ temp_g_nfsr[1] ^ temp_g_nfsr[2] ^ temp_g_nfsr[3] ^ temp_g_nfsr[4] ^ temp_g_nfsr[5] ^ temp_g_nfsr[6] ^ temp_g_nfsr[7] ^ temp_g_nfsr[8] ^ temp_g_nfsr[9] ^ temp_g_nfsr[10] ^ temp_g_nfsr[11] ^ temp_g_nfsr[12] ^ temp_g_nfsr[13] ^ temp_g_nfsr[14]
    input_nfsr = g ^ lfsr[0] ^ k ^ c4

def feedback_lfsr_is(keystream):
    input_lfsr = keystream ^ lfsr[40] ^ lfsr[35] ^ lfsr[25] ^ lfsr[20] ^ lfsr[15] ^ lfsr[6] ^ True

def feedback_nfsr_is(keystream):
    temp_g_nfsr[0] = nfsr[0]
    temp_g_nfsr[1] = nfsr[13]
    temp_g_nfsr[2] = nfsr[19]
    temp_g_nfsr[3] = nfsr[35]
    temp_g_nfsr[4] = nfsr[39]
    temp_g_nfsr[5] = (nfsr[2] and nfsr[25])
    temp_g_nfsr[6] = (nfsr[3] and nfsr[5])
    temp_g_nfsr[7] = (nfsr[7] and nfsr[8])
    temp_g_nfsr[8] = (nfsr[14] and nfsr[21])
    temp_g_nfsr[9] = (nfsr[16] and nfsr[18])
    temp_g_nfsr[10] = (nfsr[22] and nfsr[24])
    temp_g_nfsr[11] = (nfsr[26] and nfsr[32])
    temp_g_nfsr[12] = (nfsr[33] and nfsr[36] and nfsr[37] and nfsr[38])
    temp_g_nfsr[13] = (nfsr[10] and nfsr[11] and nfsr[12])
    temp_g_nfsr[14] = (nfsr[27] and nfsr[30] and nfsr[31])
    g = temp_g_nfsr[0] ^ temp_g_nfsr[1] ^ temp_g_nfsr[2] ^ temp_g_nfsr[3] ^ temp_g_nfsr[4] ^ temp_g_nfsr[5] ^ temp_g_nfsr[6] ^ temp_g_nfsr[7] ^ temp_g_nfsr[8]   ^ temp_g_nfsr[9] ^ temp_g_nfsr[10] ^ temp_g_nfsr[11] ^ temp_g_nfsr[12] ^ temp_g_nfsr[13] ^ temp_g_nfsr[14]
    input_nfsr = keystream ^ g ^ lfsr[0] ^ k ^ c4

def iv_loading():
    for i in range(70):
        iv[i] = False;
    for i in range(80):
        if(i <= 39):
            nfsr[i] = iv[i]
        elif(i >= 40 and i <= 69):
            lfsr[i - 40] = iv[i]
        elif(i >= 70 and i <= 78):
            lfsr[i - 40] = True
        else:
            lfsr[i - 40] = False
    for i in range(80):
        key[i] = False

def round_key():
    if(t <= 79):
        k = key[t]
    else:
        k = lfsr[4] ^ lfsr[21] ^ lfsr[37] ^ nfsr[9] ^ nfsr[20] ^ nfsr[29]

def output_func():
    temp_h[0] = (nfsr[4] and lfsr[6])
    temp_h[1] = (lfsr[8] and lfsr[10])
    temp_h[2] = (lfsr[17] and lfsr[32])
    temp_h[3] = (lfsr[23] and lfsr[19])
    temp_h[4] = (nfsr[4] and nfsr[38] and lfsr[32])
    h = temp_h[0] ^ temp_h[1] ^ temp_h[2] ^ temp_h[3] ^ temp_h[4]
    B = nfsr[1] ^ nfsr[6] ^ nfsr[15] ^ nfsr[17] ^ nfsr[23] ^ nfsr[28] ^ nfsr[34]
    z = h ^ lfsr[30] ^ B

def geserkiri_nfsr():
    for i in range(39):
        nfsr[i] = nfsr[i + 1]
    nfsr[39] = input_nfsr

def geserkiri_lfsr():
    for i in range(39):
        lfsr[i] = lfsr[i + 1]
    lfsr[39] = input_lfsr

def counter():
    for j in range(4):
        if(j == 0):
            for i in range(80):
                biner = str(bin(i))[2:]
                try:
                    c4_arr[i] = bool(int(biner[3]))
                    print(biner[3],biner[2],biner[1],biner[0])
                except:
                    c4_arr[i] = False
        if(j == 1):
            i = 80
            while(i < 160):
                biner = str(bin(i-80))[2:]
                try:
                     c4_arr[i] = bool(int(biner[3]))
                except:
                     c4_arr[i] = False
                i = i + 1
        if(j == 2):
            i = 160
            while(i < 240):
                biner = str(bin(i-160))[2:]
                try:
                     c4_arr[i] = bool(int(biner[3]))
                except:
                     c4_arr[i] = False
                i = i + 1
        if(j == 3):
            i = 240
            while(i < 320):
                biner = str(bin(i-240))[2:]
                try:
                     c4_arr[i] = bool(int(biner[3]))
                except:
                     c4_arr[i] = False
                i = i + 1

if __name__ == "__main__":
    iv_loading()
    counter()
    for t in range(420):
        if(t <= 319):
            round_key()
            output_func()
            keystream[t] = z
            feedback_lfsr_is(keystream[t])
            c4 = c4_arr[t]
            feedback_nfsr_is(keystream[t])
            geserkiri_nfsr()
            geserkiri_lfsr()
        else:
            round_key()
            output_func()
            keystream[t] = z
            feedback_lfsr_kg()
            c4 = c4_arr[t]
            feedback_nfsr_kg()
            geserkiri_nfsr()
            geserkiri_lfsr()
    print("KEYSTREAM : ")
    print(keystream)
