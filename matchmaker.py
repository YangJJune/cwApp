import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("cwclan-2b0c0-firebase-adminsdk-mseu6-75d2c91202.json")
firebase_admin.initialize_app(cred,{
    'databaseURL' : "https://cwclan-2b0c0-default-rtdb.firebaseio.com/"
})

while True:
    dir = db.reference()
    q=dict(dir.get())
    lastV = -1
    lastK = -1
    min = 500
    if(len(q)>1):
        #2명 이상인 경우 매치메이킹 진행
        #점수 차가 가장 가까운 사람(50점 이내) 2명 배치
        #만약 (가장 먼 점수차)/2 이상 대기했을 경우 그 둘 매칭
        q=sorted(q.items(), key=lambda x: (-x[1], x[0]))
        
        for i in range(len(q)):
            

    else:

    time.sleep(1)



"""
host = "127.0.0.1"
port = 1111
q = list()
player_map = {}

def server():
    while True:
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind((host,port))
        serverSocket.listen(1)
        print("waiting for req")

        connectionSocket,addr = serverSocket.accept()

        print("connected with ", str(addr))

        data = connectionSocket.recv(1024)
        
        tmp = data.decode("utf-8")
        tmp_arr = tmp.split(' ')
        print("received Data : ",data.decode("utf-8"))

        if(len(tmp_arr != 2)):
            #오류발생

            connectionSocket.send("ERROR 0".encode("utf-8"))
            serverSocket.close()
        else:    
            #문제 없음. 매치메이킹 진행
            q.append(tmp_arr[0])
            player_map[tmp_arr[0]] = tmp_arr[1]
            connectionSocket.send("OK".encode("utf-8"))
            print("send ack")

            serverSocket.close()
"""