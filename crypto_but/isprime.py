##############################################################
####          Vérification qu'un nombre est premier       ####
##############################################################
from math import *


def isprime(n):
    for i in range(2, int(sqrt(n)) + 1): # On teste les diviseurs de 2 à racine carrée de n
        if n % i == 0:
            return False # Si le resultat de n modulo (division euclydienne) i est 0, alors n n'est pas premier, car le reste est 0
    return True

x = int(input("Donner un nombre premier : "))
print(isprime(x))



