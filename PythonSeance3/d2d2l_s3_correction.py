from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args
import csv


# Ma fonction corrigée :
def importer_donnees(fichier):
    with open(fichier, encoding='utf-8-sig') as nat_file:
        nat_data = csv.reader(nat_file, delimiter=';')
        nat_dict = dict()
        for row in nat_data:
            if nat_data.line_num != 1:
                genre = int(row[0]) - 1  # Conversion : 0 = homme, 1 = Femme
                prenom = row[1]
                annee = int(row[2])
                # Si le prénom n'est pas présent dans la structure : intialisation
                if prenom not in nat_dict:
                    nat_dict[prenom] = {annee: [0, 0]}

                # Si l'annee n'existe pas encore pour le prénom en cours : initialisation
                if annee not in nat_dict[prenom]:  # l'année n'est pas créée
                    nat_dict[prenom][annee] = [0, 0]

                # Valorisation de l'effectif
                nat_dict[prenom][annee][genre] = int(row[3])

    return nat_dict


def ages_moyens(data):
    aver_ages = dict()
    for name in data.keys():
        calc = {0: {"sum_ages": 0, "sum_births": 0},
                1: {"sum_ages": 0, "sum_births": 0}}
        # Parcours des années enregistrées pour le prénom
        for year in data[name].keys():
            # Calcul des variables pour hommes puis femmes
            for gender, births in enumerate(data[name][year]):
                calc[gender]["sum_ages"] += (2020 - year) * births  # Somme des ages pondérée par les naissances
                calc[gender]["sum_births"] += births  # Somme des naissances

        # Initalisation du dictionnaire pour le prénom en cours
        aver_ages[name] = dict()

        # Calcul de l'age moyen pondéré total
        total_ages = calc[0]["sum_ages"] + calc[1]["sum_ages"]
        total_births = calc[0]["sum_births"] + calc[1]["sum_births"]
        aver_ages[name]["total"] = total_ages / total_births

        # Gestion du cas de division par 0 et calcul pour hommes et femmes
        if calc[0]["sum_births"] != 0:
            aver_ages[name]["hommes"] = calc[0]["sum_ages"] / calc[0]["sum_births"]

        if calc[1]["sum_births"] != 0:
            aver_ages[name]["femmes"] = calc[1]["sum_ages"] / calc[1]["sum_births"]

    return aver_ages


# Fonctions intermédiaires de sélection des données à vérifier
def verifier_donnees(fichier, prenom, annee):
    data = importer_donnees(fichier)
    return data[prenom][annee]

def verifier_aver_ages(fichier, prenom):
    data = importer_donnees(fichier)
    moyennes = ages_moyens(data)
    return moyennes[prenom]


# Liste des cas de test
inputs_import = [
    Args('nat2018_epured_5k.csv', "NICOLAS", 1984),
    Args('nat2018_r300.csv', "ALLAIN", 1956),
    Args('nat2018_n20.csv', "WALLY", 2005),
    Args('nat2018_epured_5k.csv', "_PRENOMS_RARES", 2018),
    Args('nat2018_epured_5k.csv', "MICHELINE", 1935),
    Args('nat2018_r300.csv', "RAYMONDE", 1977),
    Args('nat2018_r300.csv', "ANATOLE", 1911),
    Args('nat2018_n20.csv', "ÉYA", 2018)
]

inputs_averages = [
    Args('nat2018_epured_5k.csv', "NICOLAS"),
    Args('nat2018_r300.csv', "ALLAIN"),
    Args('nat2018_n20.csv', "WALLY"),
    Args('nat2018_epured_5k.csv', "_PRENOMS_RARES"),
    Args('nat2018_epured_5k.csv', "MICHELINE"),
    Args('nat2018_r300.csv', "RAYMONDE"),
    Args('nat2018_r300.csv', "ANATOLE"),
    Args('nat2018_n20.csv', "ÉYA")
]

# Fonctions de correction
exo_import_donnee = ExerciseFunction(
    verifier_donnees,
    inputs_import,
    layout='pprint',
    layout_args=(40, 40, 40)
)

exo_calcul_moyennes = ExerciseFunction(
    verifier_aver_ages,
    inputs_averages,
    layout='pprint',
    layout_args=(40, 40, 40)
)
