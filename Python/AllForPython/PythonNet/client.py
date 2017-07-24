from socket import *
s = socket()
host = gethostname()
#print(host)
port = 1234

s.connect((host,port))
print(s.recv(1024).decode())
