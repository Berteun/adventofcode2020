def read_board():
    f = open('input')
    return [l.strip() for l in f]

def count_trees(board, down, right):
    width = len(board[0])
    trees = 0
    pos = 0
    while pos < len(board):
        trees += board[pos][((pos//down) * right) % width] == '#'
        pos += down
    return trees

def main():
    board = read_board()
    solution = 1
    for (right, down) in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]:
        solution *= count_trees(board, down=down, right=right)
    print(solution)

if __name__ == '__main__':
    main()
