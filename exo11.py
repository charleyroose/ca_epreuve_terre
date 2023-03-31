import sys

try:
	# met hh et mm dans le même argument séparé de ":"
	hh, mm = map(int, sys.argv[1].split(":"))

	if len(sys.argv) != 2:
		print("Erreur, il ne peut y avoir qu'un seul argument sous format hh:mm")
		sys.exit()
	if hh >= 24:
		print("Erreur, l'heure ne peut pas dépasser 23")
		sys.exit()
	if hh < 00:
		print("Erreur, l'heure doit être un entier positif")
		sys.exit()
	if mm < 0:
		print("Erreur, les minutes doivent être un entier positif")
		sys.exit()
	if mm >= 60:
		print("Erreur, les minutes ne peuvent pas dépasser 59")
		sys.exit()
	
except (IndexError, ValueError):
	print("Erreur, l'argument donné doit être sous format hh:mm")

# j'utilise str.format pour avoir le 0 devant les chiffres, (index:02caractères "d" pour décimal).format puis on importe les variables hh, mm
else:
	# gère si midi donc ne change rien et rajoute pm
    if hh == 12:
        print("{0:02d}:{1:02d}PM".format(hh, mm))
    # gère si minuit, remet hh à 12 et rajoute am
    elif hh == 0:
        hh = 12
        print("{0:02d}:{1:02d}AM".format(hh, mm))
    # gère pour l'après midi, fait moins 12 et rajoute pm
    elif hh >= 13:
        hh = hh - 12
        print("{0:02d}:{1:02d}PM".format(hh, mm))
    # pour tout le reste, donc entre 01:00 à 11h59, rajoute juste am
    else:
        print("{0:02d}:{1:02d}AM".format(hh, mm))
