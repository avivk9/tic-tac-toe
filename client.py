import socket

HEADER = 64
PORT = 5050  # port number
SERVER = "192.168.1.185"  # server ipv4 adress
FORMAT = 'utf-8'
ADDR = (SERVER, PORT)    



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def send(msg):

    message = msg.encode(FORMAT)
    client.send(message)


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


def printBoard(board):
    print('\n' + board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8] + '\n')



def main():
    board = "■■■■■■■■■"
    print('\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print("Hi, welcome to \"TicTacToe\" - made by avivk9")
    print("You will need to choose which type you play - X or O")
    print("Every turn you'll need to choose the index of your placement")
    printBoard("123456789")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    
    print("\n~TO BEGIN CLICK ENTER~")

    input()

    connected = False
    while not connected:
        try:
            client.connect(ADDR)
            connected = True
        except:
            print("\n[ERORR] The enemy still not playing - wait for him to start first")
            print("hit ENTER when the enemy is ready\n")
            input()
  
    flag = True
    while flag:
        TYPE = input("\nDo you wanna be X or O? ")
        TYPE = TYPE.upper()
        if TYPE == 'X' or TYPE == 'O':
            flag = False
    
    send(TYPE)

    if TYPE == 'X':
        printBoard(board)
        board = place(board, TYPE)
        printBoard(board)
        send(board)
    if TYPE == 'O':
        send(board)
    
    
    while True:
        board = client.recv(2048).decode(FORMAT)
        print("~ENEMY'S MOVE:~")
        printBoard(board)
        if(board_statue(board, TYPE) != 'C'):
            break
        board = place(board, TYPE)
        printBoard(board)
        if(board_statue(board, TYPE) != 'C'):
            break
        send(board)
    
    end = board_statue(board, TYPE)
    if end == 'W':
        print("\n~~~~~~~~~~~~~~~")
        print("Yay! you won :)")
        print("~~~~~~~~~~~~~~~")
        send("client_won")
    if end == 'L':
        print("\n~~~~~~~~~~~~~~~")
        print("OOF! you lost :(")
        print("~~~~~~~~~~~~~~~")
        send("server_won")
    if end == 'T':
        print("\n~~~~~~~~~~~~~~~")
        print("TEKO! you tied :|")
        print("~~~~~~~~~~~~~~~")
        send("tie")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
    print("TO PLAY AGAIN JUST RUN THE PROGRAM AGAIN")
    print("■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")

main()


