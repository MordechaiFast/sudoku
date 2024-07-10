from copy import deepcopy

def possibilities(sudoku, i, j):
    digets = {*range(1,10)}
    row = {*sudoku[i]}
    col = {*([*zip(*sudoku)][j])} # flip colums to rows
    y_start = (0, 3, 6)[i//3]
    x_start = (0, 3, 6)[j//3]
    square = {sudoku[y + y_start][x + x_start]
              for y in range(3)
              for x in range(3)}
    return digets - row - col - square

def solve(sudoku: list[list[int]]):
    """using recursion and backtracking"""
    empty_cells = [(i,j)
                   for i in range(9)
                   for j in range(9)
                   if sudoku[i][j] == 0]
    if len(empty_cells) == 0:
        return sudoku
    i, j = empty_cells[0]
    for p in possibilities(sudoku, i, j):
        trial = deepcopy(sudoku)
        trial[i][j] = p
        if solution := solve(trial):
            return solution
    return False
