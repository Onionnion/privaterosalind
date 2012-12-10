with open("rosalind_subs.txt") as f:
    string = f.readline()[:-1]
    substring = f.readline()[:-1]

j = []
sublen = len(substring)

for i in range(len(string) - sublen):
    stringChunk = string[i:i + sublen]
    if substring in stringChunk:
        j.append(str(i + 1))

with open("return.txt", 'w') as f:
    for num in j:
        f.write(num + ' ')
