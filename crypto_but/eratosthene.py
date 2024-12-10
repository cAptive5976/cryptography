###################################################
####   Programmation du crible d'Eratosthène   ####
###################################################

def eratosthene(n):
    L = [] # On introduit la liste qui va contenir les nombres de 1 à n
    for i in range (2, n + 1) : 
        L.append(i) # Dans la liste on va ajouté petit a petit les nombres de 2 a n
    P = [] # On introduit la liste vide qui contiendra les nombres premiers

    while len(L) != 0 : # La boucle tourne tant-que la liste L n'est pas vide
        P.append(L[0]) # On ajoute le premier élément de L
        debut = L[0] # On crée une variable qui indique le début de la liste L 
        for k in L :
            if (k%debut)==0 : # On fait la division euclydienne 
                L.remove(L[L.index(k)]) # Si le reste de la division euclydienne est 0 on retire les non-premiers
    return P

print(eratosthene(100)) # On teste la fonction avec n = 100, donc les nombres jusqu'a 100