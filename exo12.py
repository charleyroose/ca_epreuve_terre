import sys

def convert_time_24h(hh, mm, period):
	if hh == 12 and period == "AM":
		hh = 0
		return "{0:02d}:{1:02d}".format(hh, mm)

	elif hh == 12 and period == "PM":
		return "{0:02d}:{1:02d}".format(hh, mm)

	elif hh < 12 and period == "PM":
		hh = hh + 12
		return "{0:02d}:{1:02d}".format(hh, mm)

	elif period == "AM":
		return "{0:02d}:{1:02d}".format(hh, mm)

try:
	if len(sys.argv) != 3:
		print("Erreur, il ne peut y avoir que deux arguments sous format hh:mm période")
		sys.exit()

	hh, mm, = map(int, sys.argv[1].split(":"))
	period = sys.argv[2]

	if hh < 0 or hh >= 13:
		print("Erreur, l'heure doit être entre 0 et 12")
		sys.exit()

	if mm < 0 or mm >= 60:
		print("Erreur, les minutes doivent être entre 0 et 59")
		sys.exit()

	if not period.isupper():
		print("Erreur, la période doit être écrite en majuscule")
		sys.exit()
except (IndexError, ValueError):
	print("Erreur, l'argument donné doit être sous format hh:mm période")
	sys.exit()

print(convert_time_24h(hh, mm, period))