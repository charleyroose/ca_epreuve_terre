import sys

#Vérification du nb d'arguments
if len(sys.argv) != 4:
	print("Erreur, il doit y avoir 3 arguments.")
	sys.exit()

try:
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	c = int(sys.argv[3])

	#Vérification de la différence des arguments
	if a == b or b == c or a == c:
		print("Erreur, les arguments ne peuvent pas avoir la même valeur.")
		sys.exit()

except (ValueError, IndexError):
	print("Erreur, les arguments doivent être des nombres entier.")
	sys.exit()

#test des combinaisons possible
else:
	if a < b:
		if b < c:
			print(b)
		elif a < c:
			print(c)
		else:
			print(a)

	else:
		if b > c:
			print(b)
		elif a > c:
			print(c)
		else:
			print(a)
	sys.exit()