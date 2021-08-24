def board_statue(board, TYPE):
    
    # W - TYPE WON
    # L - TYPE LOST
    # T - TIE
    # C - GAME CONTINUES

    #check if TYPE won:
    if board[0] == board[1] == board[2] == TYPE or board[3] == board[4] == board[5] == TYPE or board[6] == board[7] == board[8] == TYPE: #ROWS
        return 'W'
    if board[0] == board[3] == board[6] == TYPE or board[1] == board[4] == board[7] == TYPE or board[2] == board[5] == board[8] == TYPE: #COLUMNS
        return 'W'
    if board[0] == board[4] == board[8] == TYPE or board[2] == board[4] == board[6] == TYPE: #SLANTS
        return 'W'
    #check if TYPE lost:
    if TYPE == 'X':
        UNTYPE = 'O'
    else:
        UNTYPE = 'X'
    if board[0] == board[1] == board[2] == UNTYPE or board[3] == board[4] == board[5] == UNTYPE or board[6] == board[7] == board[8] == UNTYPE: #ROWS
        return 'L'
    if board[0] == board[3] == board[6] == UNTYPE or board[1] == board[4] == board[7] == UNTYPE or board[2] == board[5] == board[8] == UNTYPE: #COLUMNS
        return 'L'
    if board[0] == board[4] == board[8] == UNTYPE or board[2] == board[4] == board[6] == UNTYPE: #SLANTS
        return 'L'
    #check if board is full and no winner or to continiue:
    for i in range(9):
        if board[i] == '■':
            return 'C'
    return 'T'

print(board_statue("X■■O■■■■■", 'X'))