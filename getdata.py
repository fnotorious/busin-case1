import csv

flag = 1
outstanding_liens = []

with open('incorporation_liens.csv', 'r', encoding="utf8") as liens_file:
    rels_file = open('incorporation_rels.csv', 'r', encoding="utf8")
    lien_reader = csv.reader(liens_file)
    rels_reader = csv.reader(rels_file)

    l_header = next(lien_reader)
    r_header = next(rels_reader)

    for i in lien_reader:
        for j in rels_reader:
            if i[1] == j[1]:
                flag = 0
                break
        if flag == 1:
            outstanding_liens += i[1]

for i in outstanding_liens:
    print(i)
