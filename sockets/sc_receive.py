import socket
import time

def listen_for_packet():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Define the IP address and port to listen on
    ip_address = '127.0.0.1'
    port = 12345

    # Bind the socket to the IP address and port
    server_socket.bind((ip_address, port))

    # Listen for incoming packets for 5 seconds
    endT=time.time()+5
    while time.time()<endT:
        # Receive data from the socket
        data, address = server_socket.recvfrom(1024)

        # Print the received data
        print(f'Received packet from {address}: {data.decode()}')
        time.sleep(.1)

    # Close the socket
    server_socket.close()

# Call the function to start listening for packets
listen_for_packet()
