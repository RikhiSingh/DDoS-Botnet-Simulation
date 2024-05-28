'''
    This file execute the clients.py and following that the server.py
    Info about each of the file and found in themselves.
'''

# Imports
import subprocess
import time
import os

# function responsible to start the clients
def start_clients():
    # Start the client application
    deps_folder = os.path.join(os.path.dirname(__file__), 'deps')
    subprocess.Popen(['python', os.path.join(deps_folder, 'client.py')])

# main function to call start_clients() and then wait execute server.py
def main():
    # Start the client application
    start_clients()

    # Wait for the client to be ready
    time.sleep(5)  

    # Start the server application
    deps_folder = os.path.join(os.path.dirname(__file__), 'deps')
    subprocess.Popen(['python', os.path.join(deps_folder, 'server.py')])

if __name__ == "__main__":
    main()
