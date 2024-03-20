import bluetooth

def send_message(server_address, message):
    port = 1  # RFCOMM port for Bluetooth serial communication

    # Connect to the server (second terminal)
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    sock.connect((server_address, port))

    # Send the message
    sock.send(message)

    # Close the connection
    sock.close()

if __name__ == "__main__":
    # MAC address of the second terminal (server)
    server_address = "XX:XX:XX:XX:XX:XX"  # Replace with the MAC address of your second terminal

    # Message to be sent
    message = "Hello, World!"

    # Send the message
    send_message(server_address, message)
