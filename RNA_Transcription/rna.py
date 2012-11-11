DNA = open("RNA.txt").read()
RNA = ""

for char in DNA:
    if char == 'T':
        RNA += 'U'
    else:
        RNA += char

RNA_file = open("return.txt", 'w')
RNA_file.write(RNA)
RNA_file.close()
