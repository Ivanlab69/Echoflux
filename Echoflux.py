import os
import time
import hashlib
import scapy.all as scapy

# Display logo as ASCII art
def display_logo():
    logo = """
    ███████╗ ██████╗██╗  ██╗ ██████╗ ███████╗██╗     ██╗   ██╗██╗  ██╗     ██████╗ ███████╗
    ██╔════╝██╔════╝██║  ██║██╔═══██╗██╔════╝██║     ██║   ██║╚██╗██╔╝    ██╔═══██╗██╔════╝
    █████╗  ██║     ███████║██║   ██║█████╗  ██║     ██║   ██║ ╚███╔╝     ██║   ██║███████╗
    ██╔══╝  ██║     ██╔══██║██║   ██║██╔══╝  ██║     ██║   ██║ ██╔██╗     ██║   ██║╚════██║
    ███████╗╚██████╗██║  ██║╚██████╔╝██║     ███████╗╚██████╔╝██╔╝ ██╗    ╚██████╔╝███████║
    ╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚══════╝
    """
    print(logo)

# Simulate password checking with hashing
def check_password(user, password):
    stored_password_hash = hashlib.sha256("secret_password".encode()).hexdigest()
    input_password_hash = hashlib.sha256(password.encode()).hexdigest()
    return stored_password_hash == input_password_hash

# Brute force logic
def brute_force_attack(user, wordlist):
    if not os.path.exists(wordlist):
        print(f"Error: The wordlist file '{wordlist}' does not exist.")
        return

    print(f"Starting brute force attack on user: {user}...\n")

    with open(wordlist, 'r', encoding='utf-8') as file:
        passwords = file.readlines()

    passwords = [password.strip() for password in passwords]

    for count, password in enumerate(passwords, start=1):
        print(f"Attempt {count}: Trying password '{password}'...")
        if check_password(user, password):
            print(f"\n[+] Success: Password found for user '{user}': {password}")
            return
        else:
            print(f"[-] Failed: '{password}' is incorrect.")
        time.sleep(0.5)

    print(f"\n[-] Brute force failed: No password from the wordlist matched for user '{user}'.")

# Packet analyzer using Scapy
def packet_analyzer():
    print("\nStarting Packet Analyzer...\n")
    print("Press Ctrl+C to stop the analyzer.")

    # Sniffing packets using Scapy
    scapy.sniff(prn=lambda x: x.show(), store=0, count=10)  # Capture 10 packets and display details

# Metasploit integration (execute Metasploit commands)
def metasploit_interface():
    print("\nMetasploit Interface")
    print("Starting Metasploit...")

    while True:
        msf_command = input("Metasploit (msf)> ")

        if msf_command.lower() == "exit":
            break
        else:
            # You can use os.system to run Metasploit commands
            os.system(f"msfconsole -q -x \"{msf_command}\"")

# Admin Tools
def admin_tools():
    while True:
        print("\nAdmin Tools - Echoflux OS")
        print("1. Brute Force Attack")
        print("2. Packet Analyzer")
        print("3. Metasploit Interface")
        print("4. Back to Main Menu")

        choice = input("\nChoose an option: ")

        if choice == "1":
            username = input("Enter the target username: ")
            wordlist = input("Enter the path to the password wordlist file: ")
            brute_force_attack(username, wordlist)
        elif choice == "2":
            packet_analyzer()
        elif choice == "3":
            metasploit_interface()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

# Menu
def main_menu():
    while True:
        display_logo()  # Display logo each time the menu appears
        print("1. Calculator")
        print("2. Text Editor")
        print("3. Browser")
        print("4. List Directory")
        print("5. Echo Message")
        print("6. Run File")
        print("7. Admin Tools")
        print("8. Exit")
        
        choice = input("\nChoose an option: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            text_editor()
        elif choice == "3":
            browser()
        elif choice == "4":
            list_directory()
        elif choice == "5":
            echo_message()
        elif choice == "6":
            run_file()
        elif choice == "7":
            admin_tools()
        elif choice == "8":
            print("Exiting Echoflux OS...")
            break
        else:
            print("Invalid choice, please try again.")

# Placeholder functions for other menu options
def calculator():
    print("Simple Calculator (not implemented yet)")

def text_editor():
    print("Text Editor (not implemented yet)")

def browser():
    print("Browser (not implemented yet)")

def list_directory():
    print("Listing Directory (not implemented yet)")

def echo_message():
    message = input("Enter message to echo: ")
    print(message)

def run_file():
    file_name = input("Enter the file name to run: ")
    if os.path.exists(file_name):
        os.system(f"python {file_name}")
    else:
        print(f"Error: File '{file_name}' not found.")

# Run the OS
if __name__ == "__main__":
    main_menu()
