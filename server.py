import socket
import threading

HEADER = 64
PORT = 5050  # port number
SERVER = socket.gethostbyname(socket.gethostname())  # server ipv4 adress
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!disc"  # disconnecting message
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
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-----")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-----")
    print(board[6] + "|" + board[7] + "|" + board[8])



def handle_client(conn, addr):
    
    print("[~ENEMY CONNECTED - WAIT FOR HIS CHOICE~")

    connected = True
    while connected:
        msg = conn.recv(2048).decode(FORMAT)
        if msg:
            #print("MSG = " + msg)
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
                        placement = input(f"enter the index to put {TYPE} (number 1-9): ")
                        board = board[0:int(placement) - 1] + TYPE + board[int(placement):9]
                        printBoard(board)
                        if won(board):
                            print("Yay you won :)")
                            conn.close()
                            return
                        conn.send(board.encode(FORMAT))
            
        
            


            
    
    


def start():
    server.listen() 
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print("[STARTING] server i starting...")
start()


