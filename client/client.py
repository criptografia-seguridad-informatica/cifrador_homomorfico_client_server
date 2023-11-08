class Client:
    """

    """
    def __init__(self, host = 'localhost', port = 5000):
        from socket import socket

        client_socket = socket()
        client_socket.connect((host,port))

        self._socket = client_socket
    def send_message(self, message):
        self._socket.send(message.encode())

    def receive_message(self):
        return self._socket.recv(1024).decode()

    def close_connection(self):
        self._socket.close()