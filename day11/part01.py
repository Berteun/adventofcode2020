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
            nx = x + dx 
            ny = y + dy 
            if (nx < 0 or ny < 0 or ny >= len(state) or nx >= len(state[ny])):
                continue
            count += state[ny][nx] == TAKEN
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
                if get_neighbours(state, x, y) >= 4:
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
