#####################################################################
####       Programmation d'attaque du chiffrement de césar       ####
#####################################################################

from crypto import chiffrement_cesar

message = "En mathématiques, un corps est une des structures algébriques fondamentales de l'algèbre générale. C'est un ensemble muni de deux opérations binaires rendant possible l'addition, la multiplication et le calcul d'opposés et d'inverses, permettant de définir les opérateurs de soustraction et de division. La dénomination corps en français sortie de son contexte est ambigu car la définition varie selon les auteurs. Dans tous les cas, un corps est un anneau (unitaire) non nul dans lequel tout élément non nul a un inverse pour la multiplication. Dit autrement, c'est un anneau dans lequel l'ensemble des éléments non nuls est un groupe pour la multiplication. Cependant, certains auteurs1,2 exigent que la multiplication soit commutative alors que d'autres l'autorisent à ne pas l'être. Dans le cas où la définition n'exige pas la commutativité, on parle alors de corps commutatifs et de corps non commutatifs pour distinguer les corps dans lesquels la multiplication est commutative et ne l'est pas. Dans le cas où la définition exige la commutativité, l'appellation corps commutatif est alors un pléonasme. La structure algébrique qui correspond à un corps sans la contrainte de commutativité (c’est-à-dire un anneau dans lequel tout élément non nul a un inverse pour la multiplication) est alors appelée corps gauche ou anneau à division. Si la multiplication n'est pas commutative, on parle alors de corps gauches non commutatifs voire de corps non commutatifs (même s'il s’agit stricto sensu d'un oxymore) ou bien d'anneaux à division non commutatifs. On renvoie à l'article Corps commutatif qui traite le cas où la multiplication est commutative et à l’article Corps gauche qui traite le cas où la commutativité n'est pas imposée. À noter que ces distinctions sont sans importance dans le cas où le corps considéré est fini, puisque le théorème de Wedderburn assure qu'il n'existe pas de corps fini non commutatif"
k = 132
# On considère que l'attaquant ne connait pas ses variables

message_chr = chiffrement_cesar(message, k)

def stat(message_chr):
    longueur_msg = len(message_chr)
    lmg = []

    for i in range(longueur_msg):
        ascii = ord(message_chr[i])
        lmg.append(ascii)

    count_dict = {}
    for i in lmg:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    sorted_count = sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

    return sorted_count

print(stat(message_chr))

# Avec la liste on voit que le caractère qui se repete le plus est 233, or on sait que "e" (101) est le caratère le plus commun en Français
# Donc on a juste a faire 233 - 101 = 132 soit k