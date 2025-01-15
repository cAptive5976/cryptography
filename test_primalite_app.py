##############################################################
####       Test de primalité de Fermat - Application      ####
##############################################################

from crypto import test_primalite_fermat

n = 27644438

if test_primalite_fermat(n) ==  True:
    print("Le nombre n est premier")
else :
    print("Le nombre n n'est pas premier")