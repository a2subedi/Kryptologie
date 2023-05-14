def extendKeyWord(pl,keyword):
    kl = len(keyword)
    n_repeatitions = int(pl/kl)
    leftovers = pl % kl
    k_of_pl = keyword*n_repeatitions+keyword[0:leftovers]
    return k_of_pl

def encrypt(P, K):
    C = ''
    i = 0
    K_ = extendKeyWord(len(plaintext),K)
    for Pi in P:
        if Pi.isupper():
            Ci = ((ord(Pi) - 65) + (ord(K_[i]) - 65)) % 25 + 65
            C += chr(Ci)
            i+=1
        elif Pi.islower():
            Ci = ((ord(Pi) - 97) + (ord(K_[i]) - 65))  % 25+ 97
            C += chr(Ci)
            i+=1
        else:
            C += Pi
    return C

def decrypt(C, K):
    P = ''
    i = 0
    K_ = extendKeyWord(len(plaintext),K)
    for Ci in C:
        if Ci.isupper():
            Pi = (((ord(Ci) - 65) - (ord(K_[i]) - 65)) + 25) % 25 + 65
            P += chr(Pi)
            i+=1
        elif Ci.islower():
            Pi = (((ord(Ci) - 97) - (ord(K_[i]) - 65)) + 25) % 25 + 97
            P += chr(Pi)
            i+=1
        else:
            P += Ci
    return P


print('''##############################\n###### VIGENERE CIPHER  ######\n######### subedabh ###########\n\n''')
plaintext= input("Enter plaintext: ")
keyword = input("Enter keyword: ")
keyword = keyword.upper()
    
print("plaintext: ",plaintext)
extended_key = extendKeyWord(len(plaintext),keyword)

C = encrypt(plaintext,keyword)
print("ciphertext: ", C)
