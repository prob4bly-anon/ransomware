from flask import Flask, request, jsonify
import os
import requests
import json

#requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMPLEMENTOFDEFAULT"

app = Flask(__name__)

def getIp():
  ip = request.environ['HTTP_X_FORWARDED_FOR']
  return ip

@app.route('/r', methods=['POST'])
def verify_password():
    with open('logged/data.json', 'r') as f:
        config = json.load(f)
    user_id = request.json['user_id']
    password = request.json['password']
    ip = getIp()
    if user_id in config and config[user_id]['password'] == password and config[user_id]['ip'] == ip:
        key = config[user_id]['key']
        return jsonify({'key': key}), 200
    else:
        return jsonify({'error': 'Invalid password, user_id, or IP address'}), 401

@app.route('/upload_key', methods=['POST'])
def upload_key():
    user_id = request.json['user_id']
    key = request.json['key']
    with open('logged/data.json', 'r') as f:
        config = json.load(f)
    config[user_id] = {'password': 'password', 'key': key, 'ip': getIp() }
    with open('logged/data.json', 'w') as f:
        json.dump(config, f)
    return jsonify({'message': 'Key uploaded successfully.'}), 200
 

if __name__ == "__main__":
	app.run(
	host="0.0.0.0",
	port=8000,
	debug=False
	)
