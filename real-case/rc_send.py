import bluetooth

# Set up Bluetooth interface
server_mac_address = '00:00:00:00:00:00'  # Replace with the MAC address of the target Bluetooth device
port = 1  # Replace with the desired port number

# Create a Bluetooth socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

# Connect to the target device
sock.connect((server_mac_address, port))

# Send payload
payload = b'Hello, World!'  # Replace with your desired payload
sock.send(payload)

# Close the socket
sock.close()