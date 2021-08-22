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
    if board[0] == board[1] == board[2] != '.' or board[3] == board[4] == board[5] != '.' or board[6] == board[7] == board[8] != '.':
        return True
    if board[0] == board[3] == board[6] != '.' or board[1] == board[4] == board[7] != '.' or board[2] == board[5] == board[8] != '.':
        return True
    if board[0] == board[4] == board[8] != '.' or board[2] == board[4] == board[6] != '.':
        return True
    return False
    


def printBoard(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9])



def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    connected = True
    while connected:
        msg_len = conn.recv(HEADER).decode(FORMAT)
        if msg_len: 
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode(FORMAT)
            if msg == 'X':
                TYPE = 'O'
            if msg == 'O':
                TYPE = 'X'
            if msg == 'won':
                print("enemy won :(")
                conn.close()
            board = msg
            printBoard(board)
            placement = input(f"enter the index to put {TYPE} (number 1-9): ")
            board = board[0:int(placement)] + TYPE + board[int(placement) + 1:9]
            printBoard(board)
            if won(board):
                print("Yay you won :)")
                conn.close()
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


