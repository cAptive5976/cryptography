##############################################################
####       Programmation de l'échange Diffie-Hellman      ####
##############################################################
import random
from crypto import exp_fast

def main():
    p = 23
    g = 5

    #A = 6  # Cours
    #B = 15 # Cours
    A = random.randint(1, 15)
    B = random.randint(1, 15) # On ajoute des nombre aléatoire en valeur de A et B

    # Coté Alice
    # On calcul C = g^A [p]
    C = exp_fast(g, A, p)
    print(f'C = {C}')

    # Coté Bob
    # On calcul D = g^B [p]
    D = exp_fast(g, B, p)  # pas besoin de justifier dans le CR on l'a déja faits
    print(f'D = {D}')


    Ka = exp_fast(D, A, p)
    Kb = exp_fast(C, B, p)

    print(f'La clé partagé est {Ka} ou {Kb} qui sont identiques') # Justifier avec g^AB [p] dans le CR

if __name__ == '__main__':
    main()