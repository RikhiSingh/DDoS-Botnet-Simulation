'''
    This file serves as the server component, responsible for distributing the 'file.py' script 
    to all defined clients specified in "CLIENTS" and triggering their execution of the file.

    The server listens for requests from clients, providing the 'file.py' script upon request. 
    It also handles messages from clients, such as requests to fetch and execute the file.

    For each client, the server sends a request to fetch and execute the file, ensuring synchronized 
    execution of the same code on multiple client machines.
'''


import requests
from flask import Flask, request

app = Flask(__name__)

# Define the IP addresses and ports of the clients
CLIENTS = [
    'http://localhost:3001',
    'http://localhost:3002'
]

@app.route('/file', methods=['GET'])
def get_file():
    # Return the file 'file.py' from the server
    with open('file.py', 'rb') as f:
        file_content = f.read()
    return file_content, 200, {'Content-Disposition': 'attachment; filename="file.py"'}

@app.route('/receive_message', methods=['POST'])
def receive_message():
    # Handle message from clients
    # Assuming client request the file and then execute it on their side
    message = request.json
    print(f"Received message: {message}")

    if 'fetch_and_execute' in message and message['fetch_and_execute']:
        # Client requests to fetch and execute the file
        for client in CLIENTS:
            # Send a request to each client to fetch the file
            fetch_url = f"{client}/fetch_and_execute"
            response = requests.get(fetch_url)
            if response.status_code == 200:
                print(f"File fetched by client at {client} successfully")
            else:
                print(f"Failed to fetch file by client at {client}")

if __name__ == '__main__':
    app.run(port=3000)