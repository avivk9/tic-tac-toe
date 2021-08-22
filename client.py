import socket

HEADER = 64
PORT = 5050  # port number
SERVER = "192.168.1.185"  # server ipv4 adress
FORMAT = 'utf-8'
DISCONNECT_MSG = "!disc"  # disconnecting message
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


