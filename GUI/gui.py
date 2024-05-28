'''
This script creates a Tkinter GUI for controlling the client and server processes in the botnet.

It provides buttons to start the clients, start the server, stop all running processes, and show information 
about the purpose of each file.

The 'start_clients()' function initiates the client application, while 'start_server()' starts the server application.
The 'stop_processes()' function terminates all running client and server processes.
The 'show_info()' function displays information about the purpose of each file in a message box.

The GUI layout consists of buttons for each action and a status label to display messages about the current status.
'''

import tkinter as tk
from tkinter import messagebox
import subprocess
import os

# Global variables to hold references to the client and server processes
client_process = None
server_process = None

# function responsible to start the clients
def start_clients():
    global client_process
    # Start the client application
    deps_folder = os.path.join(os.path.dirname(__file__), '..', 'deps')
    client_process = subprocess.Popen(['python', os.path.join(deps_folder, 'client.py')])
    # Update status label
    status_label.config(text="Clients started successfully")

# main function to call start_clients() and then wait execute server.py
def start_server():
    global server_process
    # Start the server application
    deps_folder = os.path.join(os.path.dirname(__file__), '..', 'deps')
    server_process = subprocess.Popen(['python', os.path.join(deps_folder, 'server.py')])
    # Update status label
    status_label.config(text="Server started successfully")

# stop all the running processes
def stop_processes():
    global client_process, server_process
    # Stop the client and server processes if they are running
    if client_process:
        client_process.kill()
        client_process = None
        status_label.config(text="Processes stopped. Close the app!")
    if server_process:
        server_process.kill()
        server_process = None
        status_label.config(text="Processes stopped. Close the app!")

# show info button
def show_info():
    # Show information about the purpose of each file
    messagebox.showinfo("File Information",
                        "client.py: This file simulates a client in the DDoS botnet.\n"
                        "server.py: This file serves as the server component, distributing commands and files to the clients.")

def run_gui():
    # Create Tkinter window
    root = tk.Tk()
    root.geometry("300x230")
    root.minsize(300, 230)
    root.title("Botnet Initialization")

    # Create and pack widgets
    info_button = tk.Button(root, text="File Information", command=show_info)
    info_button.pack(pady=(10,20))

    start_clients_button = tk.Button(root, text="Start Clients", command=start_clients)
    start_clients_button.pack(pady=5)

    start_server_button = tk.Button(root, text="Start Server", command=start_server)
    start_server_button.pack(pady=5)

    stop_button = tk.Button(root, text="Stop Processes", command=stop_processes)
    stop_button.pack(pady=(18,5))

    global status_label
    status_label = tk.Label(root, text="")
    status_label.pack(pady=10)

    # Run Tkinter event loop
    root.mainloop()

# Run the GUI if this script is executed directly
if __name__ == "__main__":
    run_gui()
