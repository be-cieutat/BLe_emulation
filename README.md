# BLe_emulation
This project contains guidelines and scripts to create a virtualized connection between two bluetooth interfaces on ubuntu 2.20.4.

## /sockets
This dir is a functional demo of the project, replacing bluetooth with TCP sockets to simplify the tasks, as bluetooth controller emumation proves very challenging.

## /emulated
This dir lists my attempts at emulating bluetooth devices on a ubuntu machine, and the scripts that should be operated on such machine to communicate with a remote bluetooth device. I've covered 3 usecases:

- **a)** *no bluetooth controller available* -> **full emulation**: Using hci sockets, we simulate a bluetooth communication that actually transits through UART ports. Not yet functional. Proves challenging as the bluetooth stack on linux is quite messy. Solutions explored as of yet include native bluez btvirt emulation and emulation through the bumble python project.
- **b)** *one bluetooth controller available* -> **communication simulation**: Using a single physical controller, we simulate the behaviour of two controllers, with scripts adveritising and listening on the same interface or two interfaces linked to the same controller.
- **c)** *two bluetooth controllers* -> **real-life case**: Using two physical controllers, we use native tools from the bluez stack to communicate between both.

The stack for a) sis as follows: 
- bumble simulates a bluetooth interface
- hci (native tool) connects the interface to the os
- bluez (native tool) and pybluez lib are used to handle creating the connections and sending packets.
