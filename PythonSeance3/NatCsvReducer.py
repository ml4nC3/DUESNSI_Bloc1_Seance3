import csv

with open('nat2018.csv', encoding='utf-8') as nat_file:
    nat_data = csv.reader(nat_file, delimiter=';')
    nat_list = [row for row in nat_data]

# Créé un fichier contenant une ligne sur 300
# TODO créer le fichier si non existant
with open('nat2018_r300.csv', 'w', encoding='utf-8', newline='') as reduced_file:
    for row in nat_list[::300]:
        if row[2] != "XXXX":
            csv_writer = csv.writer(reduced_file, delimiter=';')
            csv_writer.writerow(row)

# Créé un fichier avec 1 prénom sur 20
with open('nat2018_n20.csv', 'w', encoding='utf-8', newline='') as reduced_file:
    previous_name = ''
    writing_name = ''
    count = 0
    csv_writer = csv.writer(reduced_file, delimiter=';')
    csv_writer.writerow(nat_list[0])
    for row in nat_list:
        if row[1] != previous_name:
            count += 1
        previous_name = row[1]

        if row[2] != "XXXX" and (row[1] == writing_name or count > 20):
            writing_name = row[1]
            count = 0
            csv_writer = csv.writer(reduced_file, delimiter=';')
            csv_writer.writerow(row)

# Prépare un dictionnaire des prénoms avec le total de leur nombre de naissance
mains_names = {}
for row in nat_list[1:]:
    if row[1] in mains_names:
        mains_names[row[1]] += int(row[3])
    else:
        mains_names[row[1]] = int(row[3])


# Créé un fichier avec les prénoms donnés plus de 1000 fois en tout
with open('nat2018_epured_1k.csv', 'w', encoding='utf-8', newline='') as reduced_file:
    # Ecriture des noms dont l'occurence est supérieure à la limite dans un nouveau fichier.
    csv_writer = csv.writer(reduced_file, delimiter=';')
    csv_writer.writerow(nat_list[0])
    for row in nat_list[1:]:
        if mains_names[row[1]] > 1000 and row[2] != "XXXX":
            csv_writer = csv.writer(reduced_file, delimiter=';')
            csv_writer.writerow(row)

# Créé un fichier avec les prénoms donnés plus de 5000 fois en tout
with open('nat2018_epured_5k.csv', 'w', encoding='utf-8', newline='') as reduced_file:
    # Ecriture des noms dont l'occurence est supérieure à la limite dans un nouveau fichier.
    csv_writer = csv.writer(reduced_file, delimiter=';')
    csv_writer.writerow(nat_list[0])
    for row in nat_list[1:]:
        if mains_names[row[1]] > 5000 and row[2] != "XXXX":
            csv_writer = csv.writer(reduced_file, delimiter=';')
            csv_writer.writerow(row)
