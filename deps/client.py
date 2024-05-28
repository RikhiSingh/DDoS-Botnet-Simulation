'''
    This script will run on all the clients listening to fetch
    the 'file.py' having the code that will execute on all the
    clients making them execute the same file in unison
'''

from flask import Flask
import subprocess
import requests

app = Flask(__name__)

@app.route('/fetch_and_execute', methods=['GET'])
def fetch_and_execute():
    # Fetch the file from the server and save it locally
    file_url = 'http://localhost:3000/file'
    response = requests.get(file_url)
    with open('file.py', 'wb') as f:
        f.write(response.content)
    print("File fetched successfully")

    # Execute the fetched file
    subprocess.Popen(['python', 'file.py'])
    print("File executed")

    return "File fetched and executed successfully", 200

if __name__ == '__main__':
    app.run(port=3001)  # Change port for different clients
