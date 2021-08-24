import socket
import threading

PORT = 5050  # port number
SERVER = socket.gethostbyname(socket.gethostname())  # server ipv4 adress
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'

#creating new socket      family             type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def place(board, TYPE):
    flag = True
    while flag:
        placement = input(f"enter the index to put {TYPE} (number 1-9): ")
        if(len(placement) != 1):
            print("[ERROR] too long input - PLEASE TRY AGAIN...")
        else:
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
    if board[0] == board[1] == board[2] == 'TYPE' or board[3] == board[4] == board[5] == 'TYPE' or board[6] == board[7] == board[8] == 'TYPE': #ROWS
        return 'W'
    if board[0] == board[3] == board[6] != 'TYPE' or board[1] == board[4] == board[7] != 'TYPE' or board[2] == board[5] == board[8] != 'TYPE': #COLUMNS
        return 'W'
    if board[0] == board[4] == board[8] != 'TYPE' or board[2] == board[4] == board[6] != 'TYPE': #SLANTS
        return 'W'
    #check if TYPE lost:
    if TYPE == 'X':
        UNTYPE = 'O'
    else:
        UNTYPE = 'X'
    if board[0] == board[1] == board[2] == 'UNTYPE' or board[3] == board[4] == board[5] == 'UNTYPE' or board[6] == board[7] == board[8] == 'UNTYPE': #ROWS
        return 'L'
    if board[0] == board[3] == board[6] != 'UNTYPE' or board[1] == board[4] == board[7] != 'UNTYPE' or board[2] == board[5] == board[8] != 'UNTYPE': #COLUMNS
        return 'L'
    if board[0] == board[4] == board[8] != 'UNTYPE' or board[2] == board[4] == board[6] != 'UNTYPE': #SLANTS
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



def handle_client(conn, addr):

    connected = True
    while connected:
        msg = conn.recv(2048).decode(FORMAT)
        if msg:
            if msg == 'X':
                TYPE = 'O'
            else:
                if msg == 'O':
                    TYPE = 'X'
                else:
                    if msg == 'client_won' or msg == 'server_won' or msg == 'tie':
                        if msg == 'client_won':
                            print("\n~~~~~~~~~~~~~~~")
                            print("OOF! you lost :(")
                            print("~~~~~~~~~~~~~~~")
                        
                        if msg == 'server_won':
                            print("\n~~~~~~~~~~~~~~~")
                            print("Yay! you won :)")
                            print("~~~~~~~~~~~~~~~")
                        
                        if msg == 'tie':
                            print("\n~~~~~~~~~~~~~~~")
                            print("TEKO! you tied :|")
                            print("~~~~~~~~~~~~~~~")
                        
                        conn.close()
                        return
                    else:
                        board = msg
                        print("~ENEMY'S MOVE:~")
                        printBoard(board)
                        board = place(board, TYPE)
                        printBoard(board)
                        conn.send(board.encode(FORMAT))
            
        
            


            
    
    

print("Hi, welcome to \"TicTacToe\" - made by avivk9")
print("The other user will get to choice if he play's X or O")
print("Every turn you'll need to choose the index of your placement")
printBoard("123456789")
print("\n\n~TO BEGIN CLICK ENTER~")
input()
def start():
    server.listen() 
    print("ENEMY CAN JOIN NOW")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print("ENEMY CONNECTED - WAITING FOR HIS CHOICES...")

start()


