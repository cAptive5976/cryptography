###################################################
####   Programmation de l'inversion modulo n   ####
###################################################

from .euclide_etendu import *

def inverse_modn(a,n):
    a, u, v = euclide(a,n)
    inva = u % n
    return inva
