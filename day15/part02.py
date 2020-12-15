from collections import defaultdict

def read_input():
    return [int(i) for i in open("input").readline().strip().split(",")]

LAST=30000000
def main():
    inp = read_input()
    g = defaultdict(list)
    for (i, n) in enumerate(inp):
        g[n].append(i)
    last = inp[-1]
    for n in range(len(inp), LAST):
        if len(g[last]) == 1:        
            num = 0
        else: 
            num = g[last][-1] - g[last][-2]

        if len(g[num]) <= 1:
            g[num].append(n)
        else:
            g[num][-2] = g[num][-1]
            g[num][-1] = n
        last = num
    print(last)

if __name__ == '__main__':
    main()
