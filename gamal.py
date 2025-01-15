#############################################################
####         Programmation du chiffrement de Gamal       ####
#############################################################
from crypto import big_prime_generator
from crypto import exp_fast

# Variables cours
s=7
#p=661
#a=23
M=192
k=13

p=big_prime_generator(16)
a=p-1

## Coté Alice
## On calcul Q = a^s[p]
def generate_pubkey(a,s,p):
    Q=exp_fast(a,s,p)
    pubkey = [p, a, Q]
    return pubkey

## Coté Bob
## On chiffre un message et on envoi c1 (a^k[p]) et c2 (M*(Q^k[p])
def chiffre_msg(M,k,pubkey):
    c1 = exp_fast(pubkey[1],k,pubkey[0])
    c2 = M*exp_fast(pubkey[2],k,pubkey[0])
    return c1,c2

## Coté Alice
## On déchiffre le message M par simplification
def dechiffre_msg(c1,c2,p,s):
    M = (pow(c1, (p-1-s))*c2)%p
    return M

pubkey=generate_pubkey(a,s,p)
print(f'La clé publique(p,a,Q) est {pubkey}')
c1,c2 = chiffre_msg(M,k,pubkey)
print(f'c1={c1} et c2={c2}')
Md = dechiffre_msg(c1,c2,p,s)
print(f'Le message déchiffré est Md={Md}')


