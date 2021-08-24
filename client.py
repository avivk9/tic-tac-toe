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
        placement = '?'
        while placement <'1' or placement > '9':
            placement = input(f"enter the index to put {TYPE} (number 1-9): ")
        board = board[0:int(placement) - 1] + TYPE + board[int(placement):9]
        printBoard(board)
        send(board)
    if TYPE == 'O':
        send(board)
    
    
    while not won(board):
        board = client.recv(2048).decode(FORMAT)
        print("~ENEMY'S MOVE:~")
        printBoard(board)
        placement = '?'
        while placement <'1' or placement > '9':
            placement = input(f"enter the index to put {TYPE} (number 1-9): ")
        board = board[0:int(placement) - 1] + TYPE + board[int(placement):9]
        printBoard(board)
        send(board)
    
    send("won")

main()


