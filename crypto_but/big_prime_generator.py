######################################################
####       Generateur de grand nombre premiers    ####
######################################################

import secrets

def big_prime_generator(k):
    n=secrets.randbits(k)
    return n