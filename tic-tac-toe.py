board = [[" " for x in range(3)] for y in range(3)]

def empty_cells(board):
    cells = []
    for x, cell in enumerate(board):
        if cell == ' ':
            cells.append(x)
    return cells

def valid_move(board, x):
    return x in empty_cells(board)

def move(board, x, player):
    if valid_move(board, x):
        board[x] = player
        return True
    return False

def draw(board):
    for i, cell in enumerate(board):
        if i % 3 == 0:
            print()
        print(f'| {cell} ', end='')
    print()

def evaluate(board):
    if check_win(board, 'X'):
        score = 1
    elif check_win(board, 'O'):
        score = -1
    else:
        score = 0
    return score

def check_win(board, player):
    win_conf = [
        [board[0], board[1], board[2]],
        [board[3], board[4], board[5]],
        [board[6], board[7], board[8]],
        [board[0], board[3], board[6]],
        [board[1], board[4], board[7]],
        [board[2], board[5], board[8]],
        [board[0], board[4], board[8]],
        [board[2], board[4], board[6]],
    ]
    return [player, player, player] in win_conf

def game_over(board):
    return check_win(board, 'X') or check_win(board, 'O') or len(empty_cells(board)) == 0

def minimax(board, depth, maxplayer):
    if depth == 0 or game_over(board):
        return -1, evaluate(board)
    
    if maxplayer:
        value = -float('inf')
        pos = -1
        for p in empty_cells(board):
            board[p] = 'X'
            x, score = minimax(board, depth - 1, False)
            board[p] = ' '
            if score > value:
                value = score
                pos = p
        return pos, value
    else:
        value = float('inf')
        pos = -1
        for p in empty_cells(board):
            board[p] = 'O'
            x, score = minimax(board, depth - 1, True)
            board[p] = ' '
            if score < value:
                value = score
                pos = p
        return pos, value

# 초기 게임 보드
game_board = [' ' for _ in range(9)]
player = 'X'

# 메인 프로그램
while True:
    draw(game_board)
    if len(empty_cells(game_board)) == 0 or game_over(game_board):
        break
    i, _ = minimax(game_board, 9, player == 'X')
    move(game_board, i, player)
    if player == 'X':
        player = 'O'
    else:
        player = 'X'

draw(game_board)
if check_win(game_board, 'X'):
    print('X 승리!')
elif check_win(game_board, 'O'):
    print('O 승리!')
else:
    print('비겼습니다!')