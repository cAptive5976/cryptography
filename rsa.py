#####################################################
####       Programmation du chiffrement RSA      ####
#####################################################
#M = "En mathématiques, un corps est une des structures algébriques fondamentales de l'algèbre générale."
from crypto_but.exp_mod import exp_fast
from crypto_but.inverse_modn import inverse_modn

M = "468"
import math

# Valeurs var cours
p = 17
q = 29
e = 5

def genere_clef_rsa(p,q,e):
    n = p*q #
    phi_n = (p-1)*(q-1)
    if math.gcd(phi_n,e) == 1:
        privkey = inverse_modn(e,phi_n)
        pubkey = [n,e]
        return pubkey, privkey
    else :
        print("Spécifie une autre valeur de e")

def chiffre(m, pubkey):
    x = exp_fast(m, pubkey[1], pubkey[0])
    return x

def dechiffre(x, pubkey, privkey):
    D = exp_fast(x, privkey, pubkey[0])
    return D

def main():
    pubkey, privkey = genere_clef_rsa(p,q,e)
    x = ""
    for i in range(len(M)):
        m = ord(M[i])
        x += chr(chiffre(m, pubkey))
    print(x)

    D=""
    for i in range(len(x)):
        md = ord(x[i])
        D += chr(dechiffre(md, pubkey, privkey))
    print(D)

if __name__ == "__main__":
    main()

