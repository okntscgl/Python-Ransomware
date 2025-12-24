# Ransomware Simulation – Python (Educational)

This project is a **ransomware behavior simulation written in Python**, created strictly for **educational, defensive security, and malware analysis purposes**.

It demonstrates how real-world ransomware *typically behaves* at a high level, including file encryption workflows, key handling, persistence concepts, and exfiltration-style notifications.

> ⚠️ **Legal & Ethical Disclaimer**  
> This project is provided **for educational use only**.  
> The author does **not accept any responsibility** for misuse, damage, or illegal activity resulting from this code.  
> Do **NOT** run this script outside of **isolated lab environments** (VMs, malware sandboxes).  
> Unauthorized use may violate local and international laws.

---

## Overview

The script simulates ransomware-like behavior by:

- Encrypting selected file types on a **Windows system**
- Generating a **separate decryption script**
- Sending metadata (IP address + encryption key) to a **Discord webhook**

This project is intended for:
- Malware analysis practice
- Blue team / SOC training
- Understanding ransomware kill chains
- Secure coding and defensive design awareness

---

## Key Features

### File Encryption (Simulation)
- Locates files with common extensions:
  - `.txt`, `.pdf`, `.docx`, `.jpg`, `.xlsx`
- Encrypts files using **Fernet symmetric encryption**
- Demonstrates how ransomware targets user data

### Encryption Key Handling
- Generates a unique encryption key
- Uses the same key for both encryption and decryption
- Highlights the importance of key management in ransomware families

### Discord Webhook Notification
- Sends:
  - Victim machine IP address
  - Encryption key
- Simulates **command-and-control (C2) style data exfiltration**
- Implemented only for **research demonstration**

### Decryption Script Generation
- Automatically creates a separate Python script:
  - `ransom_y.py`
- Placed on the user’s Desktop
- Allows restoration of encrypted files using the same key

### Code Obfuscation Techniques
- Uses randomly generated variable names
- Demonstrates basic obfuscation techniques used by malware authors
- Helps analysts practice code readability and reverse engineering

---

## Technical Breakdown

### Libraries Used

```python
import os
import socket
from cryptography.fernet import Fernet
import requests
import threading
import time
import random
import string
Library	Purpose
os	File system traversal
socket	IP address discovery
cryptography.fernet	File encryption
requests	Webhook communication
threading	Concurrent execution
time	Execution delays
random, string	Obfuscation / randomness

How It Works (High-Level)
System Enumeration

Retrieves local IP address

Prepares encryption environment

File Discovery

Walks through directories

Filters files by target extensions

Encryption Phase

Encrypts matching files using Fernet

Overwrites original content

Key Exfiltration (Simulation)

Sends encryption key + IP to Discord webhook

Decryption Script Generation

Creates a standalone Python script

Allows reversing the encryption process

Defensive Learning Outcomes
This project helps defenders understand:

Why offline backups are critical

How ransomware performs file discovery

The importance of egress traffic monitoring

Why webhook-based C2 is common in malware

How simple obfuscation slows analysis

Safe Usage Guidelines
✔ Run only inside:

Virtual machines

Malware labs

Isolated Windows test systems

✖ Do NOT run on:

Personal machines

Corporate networks

Production systems

Project Structure
graphql
.
├── ransomware.py     # Main ransomware simulation script
├── ransom_y.py       # Auto-generated decryption script
├── README.md         # Documentation
License
This project is licensed under the MIT License.
See the LICENSE file for details.

Final Note
Understanding how ransomware works is essential for:

Blue team defense

Incident response

Secure system design

Learning how attackers think makes defenders stronger.
