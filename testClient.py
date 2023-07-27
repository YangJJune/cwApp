from socket import *

ip = "127.0.0.1"
port = 1111

clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((ip, port))

print("연결됬음")
clientSocket.send("YangJJune 3000".encode("UTF-8"))

print("메시지 전송 완료")
data = clientSocket.recv(1024)

print("받은 데이터 : ", data.decode("UTF-8"))
clientSocket.close