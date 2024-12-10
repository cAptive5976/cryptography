#############################################################
####         Programmation du chiffrement de Gamal       ####
#############################################################
from TD.crypto_but.big_prime_generator import big_prime_generator
from TD.crypto_but.exp_mod import exp_fast

# Variables cours
s=7
p=661
a=23
M=192
k=13

# p=big_prime_generator(16)
# a=big_prime_generator(16)
# while a > p:
#     a=big_prime_generator(16)

def generate_pubkey(a,s,p):
    Q=exp_fast(a,s,p)
    pubkey = [p, a, Q]
    return pubkey

pubkey=generate_pubkey(a,s,p)
print(f'La clé publique(p,a,Q) est {pubkey}')

def chiffre_msg(M,k,pubkey):
    c1 = exp_fast(pubkey[1],k,pubkey[0])
    c2 = M*exp_fast(pubkey[2],k,pubkey[0])
    return c1,c2

c1,c2 = chiffre_msg(M,k,pubkey)
print(f'c1={c1} et c2={c2}')

def dechiffre_msg(c1,c2,p,s):
    M = (pow(c1, (p-1-s))*c2)%p
    return M

Md = dechiffre_msg(c1,c2,p,s)
print(f'Le message déchiffré est Md={Md}')