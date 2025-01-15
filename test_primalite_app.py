##############################################################
####       Test de primalité de Fermat - Application      ####
##############################################################

from crypto import test_primalite_fermat

n = 345789876545678

if test_primalite_fermat(n) ==  "true":
    print("Le nombre n est premier")
else :
    print("Le nombre n n'est pas premier")