###########################################################
####   Programmation de l'algorithm d'euclide étendu   ####
###########################################################

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

# Exemple d'utilisation avec valeurs du cours
#a, u, v = euclide(234, 35)
#print("a =", a, "u =", u, "v =", v)

