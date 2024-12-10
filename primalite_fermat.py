################################################
####       Test de primalité de Fermat      ####
################################################
import secrets

from TD.crypto_but.big_prime_generator import big_prime_generator
from crypto_but.exp_mod import exp_fast

n = 57896044618658097711785492504343953926634992332820282019728792008535319387941
print(n)

def test_primalite_fermat(n):
    a = 2
    if exp_fast(a, (n-1), n) == 1 :
        primalite = "true"
    else : primalite = "false"
    return primalite

if test_primalite_fermat(n) ==  "true":
    print("Le nombre n est premier")
else :
    print("Le nombre n n'est pas premier")
