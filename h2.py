def perm(i):
    p = []
    next_perm(i, p)

def next_perm(i, p):
    if len(p) == len(i):
        print(p)
        return
    for x in i:
        if x not in p:
            p.append(x)
            next_perm(i, p)
            p.pop()

i = [1, 2, 3]
perm(i)
