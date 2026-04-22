import socket
import platform
import os

def server_socket(type_data: str):
    
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        server_socket.bind(('0.0.0.0', 9090)) 
        server_socket.listen(1)
        print(f"\nСервер запущен на 9090-порту, ожидаем подключения...")


        conn, addr = server_socket.accept()
        print(f"Подключено: {addr}")

        if type_data == "1":

            while True:
                data = conn.recv(1024) 
                
                if not data:
                    break
                print(f"\n{data.decode('utf-8')}\n")

        elif type_data == "2":
            with open("test.txt", "wb") as file: 
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    file.write(data)
                print(f"\nФайл получен и успешно сохранен!\n")

        conn.close()

def client_socket(type_data: str):

    IP = input(f"IP: ")
    PORT = int(input(f"PORT: "))

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((IP, PORT))

    if type_data == "1":
         
        us = f"({platform.system()}) {os.getlogin()}"
        message = input(f"{os.getlogin()}: ")
        full_message = f"{us}: {message}" 
        client_socket.send(full_message.encode('utf-8'))

    elif type_data == "2":
        filename = input(f"PATH: ")
        file = open(filename, 'rb')
        print(f"\nФайл отправляется на сервер...\n")
        line = file.read(1024)

        while(line):
            client_socket.send(line)      # отправляем строку клиенту 
            line = file.read(1024)

        file.close()
    client_socket.close()

