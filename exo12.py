import sys

try:
	hh, mm, = map(int, sys.argv[1].split(":"))
	period = sys.argv[2]

	if len(sys.argv) != 3:
		print("Erreur, il ne peut y avoir que deux arguments sous format hh:mm période")
		sys.exit()
	if hh >= 13:
		print("Erreur, l'heure ne peut pas dépasser 12")
		sys.exit()
	if hh < 0:
		print("Erreur, l'heure doit être un entier positif")
		sys.exit()
	if mm < 0:
		print("Erreur, les minutes doivent être un entier positif")
		sys.exit()
	if mm >= 60:
		print("Erreur, les minutes ne peuvent pas dépasser 59")
		sys.exit()

except (IndexError, ValueError):
	print("Erreur, l'argument donné doit être sous format hh:mm période")
	sys.exit()

else:
	if hh == 12 and period == "am":
		hh = 0
		print("{0:02d}:{1:02d}".format(hh, mm))

	elif hh == 12 and period == "pm":
		print("{0:02d}:{1:02d}".format(hh, mm))

	elif hh < 12 and period == "pm":
		hh = hh + 12
		print("{0:02d}:{1:02d}".format(hh, mm))

	elif period == "am":
		print("{0:02d}:{1:02d}".format(hh, mm))