import sys

def power_result():

	try:
		nb_entier = int(sys.argv[1])
		exposant = int(sys.argv[2])
	# Vérification du nombre d'arguments
		if len(sys.argv) != 3:
			print("Erreur, il ne peut y avoir que deux arguments")
			sys.exit()

	except (ValueError, IndexError):
		print("Erreur, les arguments donné doivent être des nombres entier")
		sys.exit()
	else:
		if exposant <= 0:
			print("Erreur, l'exposant ne peut pas être supérieur ou égal à 0")
		else:
			result = nb_entier ** exposant
			print("Le résultat est", result)
			
power_result()