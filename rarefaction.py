###################################################
####          Théorème de rarefaction          ####
###################################################

import matplotlib.pyplot as plt
import numpy as np
from math import sqrt, log


# Fonction pour vérifier si un nombre est premier
def isprime(n):
    for i in range(2, int(sqrt(n)) + 1): # On teste les diviseurs de 2 à racine carrée de n
        if n % i == 0:
            return False # Si le resultat de n modulo (division euclydienne) i est 0, alors n n'est pas premier, car le reste est 0
    return True


# Fonction pour calculer pi(n)
def pi_n(n):
    compteur = 0 # On initialise un compteur à 0 qui va compter le nombre de nombres premiers
    for i in range(2, n + 1):
        if isprime(i):
            compteur += 1
    return compteur


# Fonction pour tracer les courbes, n_max represente la valeur d'arrêt du tracage, ici 10000 comme indiqué dans l'énoncé
def tracage(n_max):
    valeurs_n = np.arange(2, n_max + 1)

    # Calcul de pi(n) pour chaque n, on met le resultat dans une liste
    valeurs_pi = [pi_n(n) for n in valeurs_n]

    # On met ici les fonction d'approximation de pi(n) par Gauss et Hadamard
    # Méthode de Gauss : n / ln(n)
    gauss = valeurs_n / np.log(valeurs_n)
    # Méthode d'Hadamard : n / (ln(n) - 1.08)
    hadamard  = valeurs_n / (np.log(valeurs_n) - 1.08)

    # Ensuite on utilise matplotlib (fonction plot) pour tracer les courbes
    plt.figure(figsize=(10, 6))
    plt.plot(valeurs_n, valeurs_pi, label=r'$\pi(n)$ (nombre exact de premiers)', color='blue')
    plt.plot(valeurs_n, gauss, label=r'Gauss: $\frac{n}{\ln(n)}$', color='green', linestyle='--')
    plt.plot(valeurs_n, hadamard, label=r'Hadamard: $\frac{n}{\ln(n) - 1.08}$', color='red', linestyle='--')

    # On labelise les axes et on ajoute un titre avec les options de matplotlib
    plt.xlabel('n')
    plt.ylabel(r'pi(n)')
    plt.title('Comparaison des approximations de pi(n)')
    plt.legend()
    plt.grid(True)
    plt.show()


# On appel la fonction pour tracer les courbes avec n < 10000
tracage(1000)




