import os

file_list = []

for file in os.listdir():
    if file == "ransom_encrypt_1.py":
        continue
    if os.path.isfile(file):
        file_list.append(file)

print(file_list)