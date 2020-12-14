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

def apply_mask(dst, current_mask):
    dst_str = bin(dst)[2:].rjust(36, "0")
    mask = []
    for d,m in zip(dst_str, current_mask):
        if m == '0':
            mask.append(d)
        else:
            mask.append(m)
    return mask
        
def generate_masks(mask):
    if len(mask) == 0:
        return ['']
    masks = generate_masks(mask[1:])
    if mask[0] == 'X':
        return ['1' + m for m in masks] + ['0' + m for m in masks]
    else:
        return [mask[0] + m for m in masks]

def process(inp):
    mem = {}
    current_mask = None
    for i in inp:
        if i.type == 'm':
            current_mask = i.mask
        else:
            masked_dst = apply_mask(i.dst, current_mask)
            dests = generate_masks(masked_dst)
            for d in dests:
                mem[d] = i.val
    return mem

def main():
    inp = read_input()
    mem = process(inp)
    print(sum(v for v in mem.values()))

if __name__ == '__main__':

    main()
