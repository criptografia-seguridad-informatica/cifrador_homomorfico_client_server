from model.client import Client

if __name__ == '__main__':
    client = Client()

    message = input("Enter a number: ")
    client.send_message(message)

    received_message = client.receive_message()

    print("The server echoed the number:", received_message)

    client.close_connection()
