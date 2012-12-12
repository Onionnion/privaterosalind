from math import factorial

with open("num.txt") as f:
    try:
        num = int(f.read())
        ret = open("return.txt", 'w')
    except ValueError:
        exit("Error on file read!")


def move(e1, e2):
    """Moves an element from one list to another."""
    l2.append(l1[e2])
    l1.pop(e1)

l1 = range(1, num + 1)
l2 = []
fact = factorial(num)
ret.write(str(fact))

#for e in l1:
