import re

def count_overlaps(input):
    board = [[]]
    diag_board = [[]]
    for line in input:
        x1, y1, x2, y2 = map(int, re.split(',| -> ', line))
        board = _ensure_fits(board, x1, y1, x2, y2)
        diag_board =_ensure_fits(diag_board, x1, y1, x2, y2)
        if x1 == x2:
            y1, y2 = _smallest_first(y1, y2)
            for i in range(y1, y2 + 1):
                board[i][x1] += 1
                diag_board[i][x1] += 1
        elif y1 == y2:
            x1, x2 = _smallest_first(x1, x2)
            for j in range(x1, x2 + 1):
                board[y1][j] += 1
                diag_board[y1][j] += 1
        else:
            i = y1
            i_dir = 1 if y2 > y1 else -1
            j = x1
            j_dir = 1 if x2 > x1 else -1
            while i != y2 + i_dir and j != x2 + j_dir:
                diag_board[i][j] += 1
                i += i_dir
                j += j_dir

    overlapping_points = _count_overlap(board)
    overlapping_points_diag = _count_overlap(diag_board)
    return (overlapping_points, overlapping_points_diag)

def _smallest_first(x, y):
    return (x, y) if x < y else (y, x)

def _count_overlap(board):
    overlapping_points = 0
    for row in board:
        for val in row:
            if val >= 2:
                overlapping_points += 1
    return overlapping_points

def _ensure_fits(board, x1, y1, x2, y2):
    max_val = max(x1,y1,x2,y2)
    if max_val >= len(board):
        board = _extend_board(board, max_val + 1)
    return board

def _extend_board(board, size):
    new_board = [[0 for x in range(size)] for x in range(size)]
    for i in range(len(board)):
        for j in range(len(board[i])):
            new_board[i][j] = board[i][j]
    return new_board