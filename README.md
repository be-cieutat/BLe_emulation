# BLe_emulation
This project contains guidelines and scripts to create a virtualized connection between two bluetooth interfaces on ubuntu 2.20.4.

The stack is as follows: 
- bumble simulates a bluetooth interface
- hci (native tool) connects the interface to the os
- bluez (native tool) and pybluez lib are used to handle creating the connections and sending packets.
