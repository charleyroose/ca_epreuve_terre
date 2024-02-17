'''
24 to 12

Créez un programme qui transforme une heure affichée en format 24h en une heure affichée en format 12h.


Exemples d’utilisation :
$> python exo.py 23:40
11:40PM

Attention : midi et minuit.
'''

#déterminer si l'heure donnée est le matin ou l'apreès-midi
#gérer les cas spéciaux midi et minuit
#ne gérer que les heures car les minutes de changent pas
#juste rajouter am si l'argument est entre 01:00 et 11:59

import sys

def convert_time():
    if (len(sys.argv) !=2 or
        len(sys.argv[1]) != 5 or
        sys.argv[1][2] != ":" or
        not sys.argv[1][:2].isdigit() or
        not sys.argv[1][3:].isdigit()):
        return "erreur, veuillez n'insérer qu'un argument au format 'hh:mm'"
    else:
        hours, minutes = sys.argv[1].split(":")

        #convertir en nombre entier
        hours = int(hours)
        minutes = int(minutes)

        #vérifier que les valeurs correspondent au format horaire
        if hours > 23 or minutes > 59:
            return "erreur, les heures ne peuvent dépasser 23 et les minutes ne peuvent dépasser 59"

        #vérifier si matin ou après-midi
        period = "AM" if hours < 12 else "PM"

        #convertir en format 12h
        if hours > 12:
            hours -= 12
        elif hours == 0:
            hours = 12
    #rajouter le 0 devant chaque chiffre et assigner le résultat à une variable
    hour_12h = f"{hours:02d}:{minutes:02d}{period}"
    return hour_12h

print(convert_time())