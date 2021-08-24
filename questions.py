def place(board, TYPE):
    flag = True
    while flag:
        placement = input(f"enter the index to put {TYPE} (number 1-9): ")
        if placement <'1' or placement > '9':
            print("[ERROR] come on. A NUMBER BETWEEN 1 AND 9 - PLEASE TRY AGAIN...")
        else:
            if board[int(placement) - 1] != '■':
                print("[ERROR] THIS LOCATION HAS BEEN CHOSE ALREADY - PLEASE TRY AGAIN...")
            else:
                flag = False
        
    # return new board
    return board[0:int(placement) - 1] + TYPE + board[int(placement):9]

board = "OXX-X--O-"