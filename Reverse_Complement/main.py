with open("DNA.txt") as f:
    DNA = f.read()[::-1]
comp = ""

for char in DNA:
    if char == 'A':
        comp += 'T'
    elif char == 'T':
        comp += 'A'
    elif char == 'C':
        comp += 'G'
    elif char == 'G':
        comp += 'C'

with open("return.txt", 'w') as f:
    f.write(comp)
