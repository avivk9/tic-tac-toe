import socket

HEADER = 64
PORT = 5050  # port number
SERVER = "192.168.1.185"  # server ipv4 adress
FORMAT = 'utf-8'
DISCONNECT_MSG = "!disc"  # disconnecting message
ADDR = (SERVER, PORT)



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)



def send(msg):
    message = msg.encode(FORMAT)
    #msg_len = len(message)
    #send_len = str(msg_len).encode(FORMAT)
    #send_len += b' ' * (HEADER - len(send_len))
    #client.send(send_len)
    client.send(message)

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

def main():
    board = "■■■■■■■■■"
    print("Connected")
    flag = True
    while flag:
        TYPE = input("Do you wanna be X or O? ")
        TYPE = TYPE.upper()
        if TYPE == 'X' or TYPE == 'O':
            flag = False
    
    send(TYPE)

    if TYPE == 'X':
        printBoard(board)
        placement = input("enter the index to put X (number 1-9): ")
        board = board[0:int(placement) - 1] + TYPE + board[int(placement):9]
        printBoard(board)
        send(board)
    
    
    while not won(board):
        board = client.recv(2048).decode(FORMAT)
        print("~ENEMY'S MOVE:~")
        printBoard(board)
        placement = input(f"enter the index to put {TYPE} (number 1-9): ")
        board = board[0:int(placement) - 1] + TYPE + board[int(placement):9]
        printBoard(board)
        send(board)
    
    send("won")

main()


