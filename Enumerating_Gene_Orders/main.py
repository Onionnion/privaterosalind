from math import factorial

with open("num.txt") as f:
    try:
        num = int(f.read())
    except ValueError:
        exit("Error on file read!")


def move(e1, e2):
    """Moves an element from one list to another."""
    l2.append(l1[e2])
    del(l1[e1])

l1 = range(1, num + 1)
l2 = []
fact = factorial(num)
