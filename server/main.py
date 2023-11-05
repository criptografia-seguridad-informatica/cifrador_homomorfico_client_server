import socket

def server_program():
    host = ''
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)

    client_socket, client_address = server_socket.accept()

    number = client_socket.recv(1024).decode()
    echoed_number = number

    client_socket.send(echoed_number.encode())

    client_socket.close()

if __name__ == '__main__':
    server_program()
