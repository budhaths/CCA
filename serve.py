from flask import Flask, request, jsonify
import subprocess
import socket
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def get_privateip():
    ip = socket.gethostbyname(socket.gethostname())
    return ip
    
@app.route('/', methods=['POST'])
def call_stress_cpu():
   script_path = os.path.dirname(os.path.realpath(__file__))
   os.chdir(script_path)
   subprocess.Popen(['python', 'stress_cpu.py'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
