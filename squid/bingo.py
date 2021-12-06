def find_winner(input):
    totally_random_numbers = _get_totally_random_numbers(input)
    del input[0:2]
    boards = _make_boards(input)
    winning_score = 0
    losing_score = 0
    for number in totally_random_numbers:
        new_boards = []
        for board in boards:
            new_board = _mark_number_in_board(number, board)
            if _has_won(new_board):
                if winning_score == 0:
                    winning_score = _score(number, new_board)
                if len(boards) == 1:
                    losing_score = _score(number, new_board)
            else:
                new_boards.append(_mark_number_in_board(number, board))
        boards = new_boards
    return (winning_score, losing_score)

def _get_totally_random_numbers(input):
    totally_random_numbers = input[0]
    return map(int, totally_random_numbers.split(','))

def _make_boards(input):
    boards = []
    board = []
    row = 0
    for line in input:
        if line != "":
            board.append([])
            for number in map(int, line.split()):
                board[row].append((number, False))
            row += 1
        else:
            boards.append(board)
            board = []
            row = 0
    boards.append(board)
    return boards

def _mark_number_in_board(number, board):
    new_board = []
    for index, row in enumerate(board):
        new_board.append([])
        for value in row:
            if value[0] == number:
                new_board[index].append((number, True))
            else:
                new_board[index].append(value)
    return new_board

def _has_won(board):
    for i in range(len(board)):
        if _check_row(board[i]):
            return True
        elif _check_col([row[i] for row in board]):
            return True
    return False

def _check_row(row):
    return all([x[1] for x in row])

def _check_col(col):
    return all([x[1] for x in col])

def _score(number, board):
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not board[i][j][1]:
                sum += board[i][j][0]
    return sum * number
