from collections import namedtuple, defaultdict

Assignment = namedtuple('Assignment', ['type', 'dst', 'val'])
Mask = namedtuple('Mask', ['type', 'mask'])

def parse_line(l):
    l = l.strip()
    if l.startswith("mem"):
        dest, val = l.split(' = ')
        return Assignment('a', int(dest[4:-1]), int(val))
    else:
        _, mask = l.split(' = ')
        return Mask('m', mask);

def read_input():
    return [parse_line(l) for l in open('input')]

def split(mask):
    and_mask = ['1' if c == 'X' else '0' for c in mask]
    or_mask =  ['1' if c == '1' else '0' for c in mask]
    and_mask = int(''.join(and_mask), 2)
    or_mask = int(''.join(or_mask), 2)
    return and_mask, or_mask

def process(inp):
    mem = {}
    and_mask, or_mask = None, None
    for i in inp:
        if i.type == 'm':
            and_mask, or_mask = split(i.mask)
        else:
            v = (i.val & and_mask) | or_mask
            mem[i.dst] = v            
    return mem

def main():
    inp = read_input()
    mem = process(inp)
    print(sum(v for v in mem.values()))

if __name__ == '__main__':

    main()
