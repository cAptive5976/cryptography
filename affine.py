#####################################################
####     Programmation du chiffrement Affine     ####
#####################################################
from crypto import inverse_modn

n = 256
a = 5 # a doit être premier avec n
b = 42


def chiffre_affine(x, a, b, n):
    y = (a * x + b) %n  # on fait la formule (a * message + b)%n
    return y  

def dechiffre_affine(y, a, b, n):
    inverse_a = inverse_modn(a, n) # on récupère l'inverse de a%n 
    D = (inverse_a * (y - b)) % n # on fait la formule (a^-1 * (message_chiffré - b))%n
    return D

def main():
    M = 63

    y = chiffre_affine(M, a, b,n )

    M = "63"

    x = ""
    for i in range(len(M)):
        m = ord(M[i])
        x += chr(chiffre_affine(m, a, b, n))
    print(x)

    D=""
    for i in range(len(x)):
        md = ord(x[i])
        D += chr(dechiffre_affine(md, a,b,n))
    print(D)

if __name__ == "__main__":
    main()