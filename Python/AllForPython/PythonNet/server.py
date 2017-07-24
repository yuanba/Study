from socket import *

s = socket()
host = gethostname()
port = 1234

s.bind((host,port))

s.listen(5)

while True:
    conn , address = s.accept()
    print("Welcome to connect ",address)
    conn.send('Thank you for your connection'.encode())
    conn.close()

