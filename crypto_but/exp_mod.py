###########################################################
####      Programmation de l'exponentiation rapide     ####
###########################################################

def exp_fast(a, e, n):
    y = 1
    while e > 0:
        if e % 2 == 1:
            y = (y * a) % n
        a = (a*a)%n
        e = e // 2
    return y

# def main():
#     print("Indiqué les valeurs de a, e et n")
#     a = int(input("a = "))
#     e = int(input("e = "))
#     n = int(input("n = "))
#     y = exp_fast(a, e, n)
#     print(f'Avec notre algorithme : {y} = {a}^{e} [{n}]')
#
#
# if __name__ == "__main__":
#     main()
#
# print("Avec pow :", pow(17, 154, 100))
## La fonction pow fait la même chose, voir https://stackoverflow.com/questions/5246856/how-did-python-implement-the-built-in-function-pow