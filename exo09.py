import sys

try:
	nb_entier = int(sys.argv[1])
	#vérification du nombre d'arguments
	if len(sys.argv) != 2:
		print("Erreur, il ne peut y avoir qu'un seul argument.")
		sys.exit()
	#Vérification d'un entier positif
	if nb_entier <= 0:
		print("Erreur, l'argument donné doit être positif.")
		sys.exit()

except (IndexError, ValueError):
	print("Erreur, l'argument donné doit être un nombre entier.")
	sys.exit()
#calcul d'une racine carré est égale à nb_entier exposant 1/2
else:
	result = nb_entier ** 0.5
	print(result)
