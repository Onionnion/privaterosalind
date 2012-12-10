with open("DNA.txt") as f:
    hold = []
    s = 0
    for line in f.readlines():
        if line[0] == '>':
            hold.append((line[1:-1],))
            s = 0
        elif s == 0:
            hold[-1] = hold[-1] + (line[:-1],)
            s += 1
        else:
            hold[-1] = hold[-1][:-1] + (hold[-1][-1] + line[:-1],)
    DNA = dict(hold)
    
GC = {}

for i in DNA:
    count = 0
    length = len(DNA[i])
    for char in DNA[i]:
        if 'G' == char or 'C' == char:
            count += 1
    GCp = round(count / float(length) * 100, 3)
    GC[i] = GCp

highest = [hold[0][0], GC[hold[0][0]]]

for i in GC:
    if GC[i] > highest[1]:
        highest = [i, GC[i]]

with open("return.txt", 'w') as f:
    f.write(highest[0] + '\n')
    f.write(str(highest[1]) + '%')
