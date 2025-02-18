import socket
import platform
import hashlib

def banner():
    print(r"""
 _____     _            __ _            
| ____|___| |__   ___  / _| |_   ___  __
|  _| / __| '_ \ / _ \| |_| | | | \ \/ /
| |__| (__| | | | (_) |  _| | |_| |>  < 
|_____\___|_| |_|\___/|_| |_|\__,_/_/\_\
        Basic Multi-Tool by Ivan
    """)

def port_scanner(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            if s.connect_ex((host, port)) == 0:
                print(f"[+] Port {port} is open")
            else:
                print(f"[-] Port {port} is closed")
    except Exception as e:
        print(f"Error: {e}")

def system_info():
    print(f"System: {platform.system()}")
    print(f"Node Name: {platform.node()}")
    print(f"Release: {platform.release()}")
    print(f"Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")

def caesar_cipher(text, shift):
    encrypted = "".join(
        chr((ord(char) - 97 + shift) % 26 + 97) if char.islower() else 
        chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else char
        for char in text
    )
    print(f"Cipher Text: {encrypted}")

def file_hasher(filename):
    try:
        with open(filename, "rb") as f:
            file_hash = hashlib.sha256(f.read()).hexdigest()
            print(f"SHA256: {file_hash}")
    except FileNotFoundError:
        print("File not found!")

def main():
    banner()
    while True:
        print("\n1. Port Scanner")
        print("2. System Info")
        print("3. Caesar Cipher")
        print("4. File Hasher")
        print("5. Exit")
        
        choice = input("Select an option: ")
        
        if choice == "1":
            host = input("Enter host (e.g., 127.0.0.1): ")
            port = int(input("Enter port: "))
            port_scanner(host, port)
        elif choice == "2":
            system_info()
        elif choice == "3":
            text = input("Enter text: ")
            shift = int(input("Enter shift value: "))
            caesar_cipher(text, shift)
        elif choice == "4":
            filename = input("Enter filename: ")
            file_hasher(filename)
        elif choice == "5":
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
