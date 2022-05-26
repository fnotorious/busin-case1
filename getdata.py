import csv

flag = 1

liens = []
rels = []
outstanding_liens = []

liens_file = open('incorporation_liens.csv', 'r', encoding="utf8")
rels_file = open('incorporation_rels.csv', 'r', encoding="utf8")
lien_reader = csv.reader(liens_file)
rels_reader = csv.reader(rels_file)

l_header = next(lien_reader)
for i in lien_reader:
    liens.append(i[1])

r_header = next(rels_reader)
for j in rels_reader:
    rels.append(j[1])

for k in liens:
    for l in rels:
        if k == l:
            flag = 0
            break
    if flag == 1:
            print(k)
            outstanding_liens.append(k)
    flag = 1

print(len(outstanding_liens))

rels_file.close()

#for i in outstanding_liens:
#    print(i)
