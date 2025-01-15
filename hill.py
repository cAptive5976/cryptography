############################################################
####         Programmation du chiffrement de Hill       ####
############################################################
from crypto import determinant_mod
from crypto import inverse_modn

def chiffre_Hill(M, X, n):
    Y = [
        (M[0][0] * X[0] + M[0][1] * X[1]) % n,
        (M[1][0] * X[0] + M[1][1] * X[1]) % n
    ]
    return Y

def dechiffre_Hill(M, Y, n):
    det = determinant_mod(M, n)
    det_inv = inverse_modn(det, n)

    M_inv = [
        [(M[1][1] * det_inv) % n, (-M[0][1] * det_inv) % n],
        [(-M[1][0] * det_inv) % n, (M[0][0] * det_inv) % n]
    ]

    X = [
        (M_inv[0][0] * Y[0] + M_inv[0][1] * Y[1]) % n,
        (M_inv[1][0] * Y[0] + M_inv[1][1] * Y[1]) % n
    ]
    return X

def main():
    n = 7
    M = [[2, 1], [3, 4]]
    X = [3, 2]

    Y = chiffre_Hill(M, X, n)
    print("Message chiffré :", Y)

    X_dechiffre = dechiffre_Hill(M, Y, n)
    print("Message déchiffré :", X_dechiffre)

if __name__ == "__main__":
    main()
