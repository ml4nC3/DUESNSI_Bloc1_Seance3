from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args
import csv


# Ma fonction corrigée :
def importer_donnees(fichier):
    with open(fichier, encoding='utf-8-sig') as nat_file:
        nat_data = csv.reader(nat_file, delimiter=';')
        nat_list = []
        for row in nat_data:
            if nat_data.line_num == 1:
                nat_list.append(row)
            else:
                nat_list.append([row[0], row[1], int(row[2]), int(row[3])])
    return nat_list


def verifier_donnees(fichier, index):
    liste = importer_donnees(fichier)
    return liste[index]


inputs_import = [
    Args('nat2018_epured_5k.csv', 1045),
    Args('nat2018_r300.csv', 24),
    Args('nat2018_n20.csv', 12960),
    Args('nat2018_epured_5k.csv', 386),
    Args('nat2018_epured_5k.csv', 85033),
    Args('nat2018_r300.csv', 1043),
    Args('nat2018_r300.csv', 2121),
    Args('nat2018_n20.csv', 30083),
]
# Liste des cas de test

# Fonction de correction
exo_import_donnee = ExerciseFunction(
    verifier_donnees,
    inputs_import,
    layout='pprint',
    layout_args=(40, 40, 40)
)

