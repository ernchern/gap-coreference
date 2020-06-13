import csv

writeList = []
with open("gap-development.tsv", 'r') as f:
    reader = csv.DictReader(f, fieldnames=['ID', 'Text', 'Pronoun', 'Pronoun-offset', 'A', 'A-offset', 'A-coref', 'B','B-offset', 'B-coref', 'URL'], delimiter='\t')
    next(reader, None)
    for row in reader:
        writeList.append([row['ID'],row['A-coref'],row['B-coref']])
        
with open("gap-development-copy.tsv", 'w', newline='') as f:
    writer = csv.writer(f, delimiter='\t')
    writer.writerows(writeList)
    
