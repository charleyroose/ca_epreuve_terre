'''
12 to 24

Créez un programme qui transforme une heure affichée en format 12h en une heure affichée au format 24h.


Exemples d’utilisation :
$> python exo.py 11:40PM
23:40

Attention : midi et minuit.
'''

import sys

def convert_time():
    if (len(sys.argv) != 2 or
        len(sys.argv[1]) != 7 or
        sys.argv[1][2] != ":" or
        not sys.argv[1][:2].isdigit() or
        not sys.argv[1][3:5].isdigit() or
        not sys.argv[1][5:].upper() in ("AM", "PM")):
        return "erreur, veuillez n'insérer qu'un argument au fortmat 'hh:mmpp', pp étant la période."
    else:
        hours, minutes, period = sys.argv[1][:2], sys.argv[1][3:5], sys.argv[1][5:].upper()

        #convertir en nombre entier
        hours = int(hours)
        minutes = int(minutes)

        #vérifier si les valeurs conviennent au format horaire
        if hours not in range(1, 13) or minutes > 59:
            return "erreur, les heures doivent être entre 01 et 12, les minutes ne peuvent dépasser 59"
        
        #convertir en format 24h
        if hours == 12 and period == "AM":
            hours = 0
        elif period == "PM":
            if hours != 12:
                hours += 12
            else:
                hours = 12
        
        #rajouter le 0 devant chaque chiffre et assigner le résultat à une variable
        hours_24 = f"{hours:02d}:{minutes:02d}"
        return hours_24

print(convert_time())