import bluetooth

def receive_message():
    port = 1  # RFCOMM port for Bluetooth serial communication

    # Create a server socket
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.bind(("", port))
    server_sock.listen(1)

    # Accept incoming connections
    client_sock, client_info = server_sock.accept()
    print("Accepted connection from", client_info)

    # Receive the message
    data = client_sock.recv(1024)
    print("Received message:", data.decode())

    # Close the connection
    client_sock.close()
    server_sock.close()

if __name__ == "__main__":
    receive_message()
