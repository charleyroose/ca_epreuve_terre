import sys

try:
	arg = sys.argv[1]
except (IndexError, ValueError):
	print("Erreur")
else:
	print(arg[::-1])	#j'utilise cette syntaxe pour extraire une sous-séquence de 'arg' en commençant par la fin, en allant jusqu'au début en itérant de manière croissante