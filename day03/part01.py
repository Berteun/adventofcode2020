def read_board():
    f = open('input')
    return [l.strip() for l in f]

def count_trees(board, down, right):
    width = len(board[0])
    trees = 0
    pos = 0
    while pos < len(board):
        trees += board[pos][(pos * right) % width] == '#'
        pos += down
    return trees

def main():
    board = read_board()
    trees = count_trees(board, down=1, right=3)
    print(trees)

if __name__ == '__main__':
    main()
