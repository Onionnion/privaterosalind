from codon import codons

with open("test.txt") as f:
    DNA = f.readline()[:-1]

RNA = ""
codon = ""

for char in DNA:
    if char == 'T':
        RNA += 'U'
    else:
        RNA += char

goOn = False

for i in range(0, len(RNA), 3):
    if RNA[i:i+3] in codons:
        cod = codons[RNA[i:i+3]]
        if goOn == False:
            if cod == 'M':
                codon += cod
                goOn = True
        else:
            if cod == '\n':
                codon += cod
                GoOn = False
            else:
                codon += cod

print codon
