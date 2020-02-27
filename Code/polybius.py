def encrypt(plain):
    try:
        assert plain.isalpha()
        plain = plain.lower()
        for char in plain:
            row = int((ord(char) - ord('a')) / 5) + 1
            col = ((ord(char) - ord('a')) % 5) + 1
            if char == 'k':
                row = row - 1
                col = 5 - col + 1
            elif ord(char) >= ord('j'):
                if col == 1 :
                    col = 6
                    row = row - 1
                col = col - 1
            print(row, col, end =' ', sep ='')
        print("")
    except:
        print("Opps, Somethin Went Wrong")

def decrypt(cipher):
    #try:
        cipher = "".join(cipher.split())
        table = [["a","b","c","d","e"],
                 ["f","g","h","i/j","k"],
                 ["l","m","n","o","p"],
                 ["q","r","s","t","u"],
                 ["v","w","x","y","z"]]
        val = ""
        n = 2
        jump = [cipher[i:i+n] for i in range(0, len(cipher),n)]
        for num in jump:
            row = int(num[:1]) - 1
            col = int(num[1:]) - 1
            val += table[row][col]
        print(val)

    #except:
     #   print("Opps, Somethin Went Wrong")

if __name__ == "__main__":
    plain = input("plain: ")
    encrypt(plain)
    cipher = input("cipher: ")
    decrypt(cipher)
