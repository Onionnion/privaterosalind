dna = open("rosalind_dna.txt").read()
A = 0
C = 0
G = 0
T = 0

for char in dna:
    if char == 'A':
        A += 1
    elif char == 'C':
        C += 1
    elif char == 'G':
        G += 1
    elif char == 'T':
        T += 1

print "%d %d %d %d" % (A, C, G, T)
