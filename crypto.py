#################################################################
####       Module des fonction externes de cryptographie     ####
#################################################################

import secrets
from math import sqrt

######################################################

# Génerateur de grand nombre premiers
def big_prime_generator(k):
    while True:
        n=secrets.randbits(k)
        if test_primalite_fermat(n):
            return n
######################################################

# Test de primalité de Fermat
def test_primalite_fermat(n):
    a = 2
    if exp_fast(a, (n-1), n) == 1 :
        primalite = True
    else : primalite = False
    return primalite

######################################################

# Vérification qu'un nombre est premier
def isprime(n):
    for i in range(2, int(sqrt(n)) + 1): # On teste les diviseurs de 2 à racine carrée de n
        if n % i == 0:
            return False # Si le resultat de n modulo (division euclydienne) i est 0, alors n n'est pas premier, car le reste est 0
    return True

######################################################

# Programmation de l'inversion modulo n
def inverse_modn(a,n):
    a, u, v = euclide(a,n)
    inva = u % n
    return inva

######################################################

# Programmation de l'exponentiation modulaire rapide
def exp_fast(a, e, n):
    y = 1
    while e > 0:
        if e % 2 == 1:
            y = (y * a) % n
        a = (a*a)%n
        e = e // 2
    return y

######################################################

# Programmation de l'algorithm d'euclide étendu
def euclide(a, b):
    u = 1
    v = 0
    up = 0
    vp = 1
    if b > a:
        atemp = a
        a = b
        b = atemp
        u = 0
        v = 1
        up = 1
        vp = 0

    if b > 0:
        while b > 0 :
            r = a % b
            q = a // b
            a = b
            b = r
            upp =  u - q * up
            vpp = v - q * vp
            u = up
            v = vp
            up = upp
            vp = vpp
        return a, u, v
    else:
        print("La condition b > 0 n'a pas été respecté")

######################################################

# Programmation du crible d'Eratosthène
def eratosthene(n):
    L = [] # On introduit la liste qui va contenir les nombres de 1 à n
    for i in range (2, n + 1) :
        L.append(i) # Dans la liste on va ajouté petit a petit les nombres de 2 a n
    P = [] # On introduit la liste vide qui contiendra les nombres premiers

    while len(L) != 0 : # La boucle tourne tant-que la liste L n'est pas vide
        P.append(L[0]) # On ajoute le premier élément de L
        debut = L[0] # On crée une variable qui indique le début de la liste L
        for k in L :
            if (k%debut)==0 : # On fait la division euclydienne
                L.remove(L[L.index(k)]) # Si le reste de la division euclydienne est 0 on retire les non-premiers
    return P

######################################################

# Programmation du chiffrement de césar
def chiffrement_cesar(message, k):
    longeur_msg = len(message)
    message_crypte = ""

    for i in range(longeur_msg):
        if message[i] == " ":
            message_crypte += chr(255)
            continue

        ascii = ord(message[i]) + k
        message_crypte += chr(ascii)
    return message_crypte


def dechiffrement_cesar(message_chr, k):
    longeur_chr = len(message_chr)
    message = ""

    for i in range(longeur_chr):
        if message_chr[i] == chr(255):
            message += " "
            continue

        ascii = ord(message_chr[i]) - k
        message += chr(ascii)
    return message

######################################################

# Programmation du calcul de determinant de matrice mod(n)
def determinant_mod(M, n):
    d = (M[0][0] * M[1][1] - M[0][1] * M[1][0]) % n
    return d