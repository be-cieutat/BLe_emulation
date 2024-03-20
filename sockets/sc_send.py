import socket
import random
import time


def send_packet():
    # Define the target socket address
    target_ip = '127.0.0.1'  # Replace with the IP address of the target socket
    target_port = 12345  # Replace with the port number of the target socket

    # Create a socket object
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Generate a random value
    random_value = random.randint(1, 100)

    # Convert the random value to bytes
    packet_data = str(random_value).encode()

    # Send the packet to the target socket
    sock.sendto(packet_data, (target_ip, target_port))

    # Close the socket
    sock.close()

#main
endT=time.time()+5
while time.time()<endT:
    send_packet()
    time.sleep(0.1)