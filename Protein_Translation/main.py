from codon import codons

with open("rosalind_prot.txt") as f:
    RNA = f.readline()

protein = []

for i in range(0, len(RNA), 3):
    if RNA[i:i+3] in codons:
        protein.append(codons[RNA[i:i+3]])

with open("return.txt", 'w') as f:
    for char in protein:
        f.write(char)
