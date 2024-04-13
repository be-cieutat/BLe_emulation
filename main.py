import os
import random
import time

# Get the absolute path of the script directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the paths to the scripts
sc_read_path = os.path.join(script_dir, 'socket', 'sc_read.py')
sc_send_path = os.path.join(script_dir, 'socket', 'sc_send.py')

# Run sc_read.py in a terminal
os.system(f"python {sc_read_path}")

# Generate and send random payloads every 1 second
while True:
    # Generate a random payload
    payload = random.randint(0, 100)

    # Run sc_send.py with the payload as an argument in a terminal
    os.system(f"python {sc_send_path} {payload}")

    # Wait for 1 second
    time.sleep(1)