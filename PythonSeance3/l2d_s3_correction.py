from nbautoeval.exercise_function import ExerciseFunction
from nbautoeval.args import Args
import csv


# Ma fonction corrigée :
def importer_donnees(fichier):
    with open(fichier, encoding='utf-8-sig') as nat_file:
        nat_data = csv.reader(nat_file, delimiter=';')
        nat_list = []
        for row in nat_data:
            if nat_data.line_num != 1:
                nat_list.append({"sexe": row[0], "prenom": row[1], "annee": int(row[2]), "effectif": int(row[3])})
    return nat_list


def ages_moyens(datas):
    aver_ages = [{"sexe": datas[0]["sexe"], "prenom": datas[0]["prenom"]}]  # Initialisation du premier nom de la liste
    sum_ages, sum_count = 0, 0  # Initialisation des variables de comptage

    for record in datas:
        if (record["sexe"], record["prenom"]) == (aver_ages[-1]["sexe"], aver_ages[-1]["prenom"]):
            # Si le sexe et le nom sont égaux à l'enregistrement en cours
            sum_ages = sum_ages + (2020 - record["annee"]) * record[
                "effectif"]  # Calcul de l'age pondéré par l'effectif
            sum_count = sum_count + record["effectif"]  # Calcul des effectifs totaux (dénominateur)
        else:
            # Si le nom change on ajoute l'age moyen à la dernière ligne
            aver_ages[-1]["average"] = sum_ages / sum_count
            aver_ages.append(
                {"sexe": record["sexe"], "prenom": record["prenom"]})  # Ajout du nouveau nom dans une nouvelle ligne
            sum_ages = (2020 - record["annee"]) * record["effectif"]  # Calcul du premier age pondéré
            sum_count = record["effectif"]  # Initialisation de la somme des effectifs

    aver_ages[-1][
        "average"] = sum_ages / sum_count  # On met à jour l'age moyen du dernier prénom dans la dernière ligne
    return aver_ages


# Fonctions intermédiaires de sélection des données à vérifier
def verifier_donnees(fichier, index):
    liste = importer_donnees(fichier)
    return liste[index]

def verifier_aver_ages(fichier, index):
    liste = importer_donnees(fichier)
    moyennes = ages_moyens(liste)
    return int(moyennes[index]["average"])


# Liste des cas de test
inputs_import = [
    Args('nat2018_epured_5k.csv', 1045),
    Args('nat2018_r300.csv', 24),
    Args('nat2018_n20.csv', 12960),
    Args('nat2018_epured_5k.csv', 386),
    Args('nat2018_epured_5k.csv', 85032),
    Args('nat2018_r300.csv', 1043),
    Args('nat2018_r300.csv', 2010),
    Args('nat2018_n20.csv', 30081)
]

inputs_averages = [
    Args('nat2018_epured_5k.csv', 1045),
    Args('nat2018_r300.csv', 24),
    Args('nat2018_n20.csv', 58),
    Args('nat2018_epured_5k.csv', 386),
    Args('nat2018_epured_5k.csv', 1135),
    Args('nat2018_r300.csv', 1000),
    Args('nat2018_r300.csv', 2010),
    Args('nat2018_n20.csv', 1690)
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
