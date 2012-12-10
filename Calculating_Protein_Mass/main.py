from mass import masses

with open("rosalind_prtm.txt") as f:
    P = f.readline()[:-1]

weight = 0.0

for char in P:
    weight += masses[char]

weight = round(weight, 3)

with open("return.txt", 'w') as f:
    f.write(str(weight))
