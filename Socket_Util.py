import threading
import socket
from _thread import *


class Socket_Process(threading.Thread):
    def __init__(self):
        super().__init__()
        print('Socket server init')
        self.host = '192.168.0.9'
        self.port = 3333
        self.cmd = ''

    def run(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((self.host, self.port))
        server_socket.listen()
        print('Socket server start')

        # 새로운 쓰레드에서 해당 소켓을 사용하여 통신을 하게 됩니다.
        while True:
            print('wait')

            client_socket, addr = server_socket.accept()
            start_new_thread(self.threaded, (client_socket, addr))

    # def socketSend(self, message):
    #     self.clientSocket.send(message.encode("utf-8"))

    # 접속한 클라이언트마다 새로운 쓰레드가 생성되어 통신을 하게 됩니다. 
    def threaded(self, client_socket, addr): 
        print('Connected by :', addr[0], ':', addr[1]) 

        # 클라이언트가 접속을 끊을 때 까지 반복합니다. 
        while True:
            try:
                # data = client_socket.recv(1024)

                # if not data: 
                #     print('Disconnected by ' + addr[0],':',addr[1])
                #     break

                # print('Received from ' + addr[0],':',addr[1] , data.decode())
                
                cmd = input("cmd ? ")

                if cmd == "ON":
                    client_socket.send("CONTROL_ON_1\n".encode("utf-8"))
                    print("CONTROL_ON_1")
                elif cmd == "OFF":
                    client_socket.send("CONTROL_OFF_1\n".encode("utf-8"))
                    print("CONTROL_OFF_1")
                elif cmd == "RESET":
                    client_socket.send("RESET_1\n".encode("utf-8"))
                    print("RESET_1")

            except ConnectionResetError as e:
                print('Disconnected by ' + addr[0],':',addr[1])
                break
                
        self.disConnect()