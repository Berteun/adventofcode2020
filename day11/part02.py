FLOOR = "."
SEAT  = "L"
TAKEN = "#"

def read_input():
    floor = [list(l.strip()) for l in open("input")]
    return floor

def get_neighbours(state, x, y):
    count = 0
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            if dx == dy == 0:
                continue
            mult = 1
            nx = x + dx  
            ny = y + dy 
            while (nx >= 0 and ny >= 0 and ny < len(state) and nx < len(state[ny])):
                if state[ny][nx] == TAKEN:
                    count += 1
                    break
                if state[ny][nx] == SEAT:
                    break
                mult += 1
                nx = x + dx * mult
                ny = y + dy * mult
    return count

def step(state):
    new_state = []
    for (y, r) in enumerate(state):
        new_row = []
        for (x, p) in enumerate(r):
            if p == FLOOR:
                new_row.append(FLOOR)
            elif p == SEAT:
                if get_neighbours(state, x, y) == 0:
                    new_row.append(TAKEN)  
                else:
                    new_row.append(SEAT)  
            elif p == TAKEN:
                if get_neighbours(state, x, y) >= 5:
                    new_row.append(SEAT)  
                else:
                    new_row.append(TAKEN)  
        new_state.append(new_row)
    return new_state


def evolve(state):
    prev_state = None
    while prev_state != state:
        prev_state = state
        state = step(state)
    return state

def main():
    state = read_input()
    final = evolve(state)
    #print('\n'.join(''.join(r) for r in final))
    print(sum(r.count(TAKEN) for r in final))

if __name__ == '__main__':
    main()
