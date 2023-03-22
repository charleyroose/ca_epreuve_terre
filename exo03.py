import sys

letter = sys.argv[1]
arg = range(ord('a'), ord('z')+1)
var = letter

for num in arg:
	print(var, end="")			#sort chaque itération de la boucle en enlevant le retour à la ligne
	if var == "z":				#stop la boucle lorsque la valeur = z
		break
	var = chr(ord(var) + 1)		#transforme la lettre en valeur numérique, ajoute 1 et transforme le résultat en lettre correspondante
print()							#ajoute un retour à la ligne