import socket
import threading

HEADER = 64
PORT = 5050  # port number
SERVER = socket.gethostbyname(socket.gethostname())  # server ipv4 adress
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
TYPE = 'O'

#creating new socket      family             type
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def won(board):
    if board[0] == board[1] == board[2] != '■' or board[3] == board[4] == board[5] != '■' or board[6] == board[7] == board[8] != '■':
        return True
    if board[0] == board[3] == board[6] != '■' or board[1] == board[4] == board[7] != '■' or board[2] == board[5] == board[8] != '■':
        return True
    if board[0] == board[4] == board[8] != '■' or board[2] == board[4] == board[6] != '■':
        return True
    return False
      


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
                    if msg == 'won':
                        print("enemy won :(")
                        conn.close()
                    else:
                        board = msg
                        print("~ENEMY'S MOVE:~")
                        printBoard(board)
                        placement = '?'
                        while placement <'1' or placement > '9':
                            placement = input(f"enter the index to put {TYPE} (number 1-9): ")
                        board = board[0:int(placement) - 1] + TYPE + board[int(placement):9]
                        printBoard(board)
                        if won(board):
                            print("Yay you won :)")
                            conn.close()
                            return
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


