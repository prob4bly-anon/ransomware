# Ransomware

## Server

The server-side code is written in Python using the Flask microframework. The server is responsible for verifying the password and providing the decryption key to the client.

### Requirements

- Flask
- json

### Usage

1. Start the server by running `python app.py`
2. The server will listen on `http://localhost:8000/` by default. (Better host it somewhere)
3. The server has 2 routes:
   - `/r` for password verification
   - `/upload_key` for uploading the encryption key
4. The server expects a JSON object with the following fields:
   - `user_id`: the unique identifier of the client
   - `password`: the password to verify
   - `key`: the encryption key (for `/upload_key` route)
5. The server will return a JSON object with the following fields:
   - `key`: the decryption key (if the password is correct)
   - `error`: error message (if the password is incorrect)

## Client

The client code encrypts files on the specified directory. It communicates with the server to verify the password and upload the encryption key.

### Requirements

- cryptography
- requests

### Usage

0. Edit `password_verification_url` & `key_upload_url` variable with your own URL in src/main.py
1. Run `python main.py`
2. The script will prompt for a password
3. The script will encrypt all files in the specified directory (`/path/to/directory` by default)
4. The script will upload the encryption key to the server
5. To decrypt the files, run the script again and enter the correct password

- Any improvement to the program is appreciated, happy coding! :)

