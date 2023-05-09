import sys

#test des combinaisons possible
def find_switzerland():
	if a < b:
		if b < c:
			return b
		elif a < c:
			return c
		else:
			return a

	else:
		if b > c:
			return b
		elif a > c:
			return c
		else:
			return a
			
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


print(find_switzerland())