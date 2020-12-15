from collections import defaultdict

def read_input():
    return [int(i) for i in open("input").readline().strip().split(",")]

def main():
    inp = read_input()
    g = defaultdict(list)
    for (i, n) in enumerate(inp):
        print(i + 1, n)
        g[n].append(i)
    last = inp[-1]
    for n in range(len(inp), 2020):
        #print(g,last,g[last])
        if len(g[last]) == 1:        
            num = 0
            g[0].append(n)
        else: 
            d = g[last][-1] - g[last][-2]
            num = d
            g[d].append(n)
        last = num
    print(last)

if __name__ == '__main__':
    main()
