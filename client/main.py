import socket

def client_program():
    host = 'localhost'
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    number = input("Enter a number: ")
    client_socket.send(number.encode())

    echoed_number = client_socket.recv(1024).decode()
    print("The server echoed the number:", echoed_number)

    client_socket.close()

if __name__ == '__main__':
    client_program()
