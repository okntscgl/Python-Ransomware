# Ransomware Python Script

## Overview

This script is a simple demonstration of ransomware-like functionality that encrypts specified file types on a Windows machine. It generates a decryption script and sends a notification message to a Discord webhook, including the system's IP address and the encryption key used. **This code is for educational purposes only and should never be used maliciously.**

## Features

- **File Encryption**: 
  - The script identifies and encrypts files with specified extensions such as `.txt`, `.pdf`, `.docx`, `.jpg`, and `.xlsx` found within the file system.
  
- **Discord Webhook Notification**: 
  - It sends a notification containing the victim's IP address and the encryption key to a specified Discord webhook URL, enabling the attacker to receive the key easily.
  
- **Decryption Script Creation**: 
  - A separate Python script (`ransom_y.py`) is generated on the user's desktop, which can be used to decrypt the previously encrypted files, allowing the victim to regain access to their data.
  
- **Random Variable Naming**: 
  - To obfuscate the code and make it harder to read, the script employs randomly generated variable names, adding an extra layer of complexity.

## Script Breakdown

### Imports

The script uses the following libraries:

```python
import os
import socket
from cryptography.fernet import Fernet
import requests
import threading
import time
import random
import string

This script is provided for educational purposes only. The author does not accept any legal responsibility for any misuse of this script or any consequences that may arise from its use. Please use this code within legal boundaries and for ethical hacking practices only.
