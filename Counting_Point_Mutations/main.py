with open("DNA.txt") as f:
    first = f.readline()
    secnd = f.readline()

if len(first) > len(secnd):
    length = len(secnd)
elif len(first) < len(secnd):
    length = len(first)
Hd = 0

for i in range(length):
    if first[i] != secnd[i]:
        Hd += 1

with open("return.txt", 'w') as f:
    f.write(first)
    f.write(secnd)

print Hd
