def read_input():
    inp = []
    for l in open("input"):
        c = l.index("(contains ")
        if c > -1:
            ingredients = l[:c].strip().split()
            allergens = l[c+9:].strip()[:-1].split(", ")
        else:
            allergens = []
            ingredients = l.strip().split()
        inp.append((set(ingredients), set(allergens)))
    return inp

def unsolved(g):
    return any(len(v) > 1 for v in g.values())

def reduce_sol(g): 
    while unsolved(g):
        for (k, v) in g.items():
            if len(v) == 1:
                for (ok, ov) in g.items():
                    if len(ov) > 1:
                        g[ok].difference_update(v)
    return g

def process(inp):
    all_allergens = set()
    for (ings, alls) in inp:
        all_allergens.update(alls)

    g = {}
    for allergen in all_allergens:
        possible = set.intersection(*[ings for (ings, alls) in inp if allergen in alls])
        g[allergen] = possible 

    g = reduce_sol(g)

    return sorted((a, v.pop()) for (a, v) in g.items())


def main():
    inp = read_input()
    unsafe = process(inp)
    print(','.join(u[1] for u in unsafe))


if __name__ == '__main__':
    main()
