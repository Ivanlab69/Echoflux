import os
import subprocess
import time
import hashlib
import nmap
import sys

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

# Help menu
def display_help():
    print("""
    Echoflux OS Help Menu:
    1. Open Lynx Browser
    2. Open Terminal Shell
    3. Run Nmap Scan
    4. Exit

    Type the option number to select a tool or 'exit' to quit.
    """)

# Open Lynx Browser
def start_lynx():
    print("Starting Lynx browser...")
    url = input("Enter URL to visit: ")
    os.system(f"lynx {url}")

# Open Terminal Shell
def start_shell():
    print("Opening shell terminal...")
    os.system("bash")  # Opens the standard bash shell

# Run Nmap Scan
def run_nmap():
    print("Starting Nmap scan...")
    target = input("Enter the IP address or hostname for Nmap scan: ")
    scanner = nmap.PortScanner()
    print(f"Scanning {target}...")
    scanner.scan(target, '1-1024')  # Scans ports 1-1024
    print(scanner.all_hosts())
    for host in scanner.all_hosts():
        print(f"Host: {host}")
        print(f"State: {scanner[host].state()}")
        for protocol in scanner[host].all_protocols():
            print(f"Protocol: {protocol}")
            lport = scanner[host][protocol].keys()
            for port in lport:
                print(f"Port: {port}, State: {scanner[host][protocol][port]['state']}")
    print("Scan completed.")

# tmux-like interface with multiple windows
def open_tmux():
    print("Opening tmux-like terminal...")
    while True:
        display_help()
        option = input("Select an option: ")
        if option == '1':
            start_lynx()
        elif option == '2':
            start_shell()
        elif option == '3':
            run_nmap()
        elif option == '4':
            print("Exiting Echoflux OS...")
            break
        else:
            print("Invalid option. Type 'help' for options.")
        time.sleep(1)

# Main entry function
def main():
    os.system('clear')  # Clears the terminal screen
    display_logo()

    while True:
        command = input("Echoflux OS> ")
        if command == 'help':
            display_help()
        elif command == 'start':
            open_tmux()
        elif command == 'exit':
            print("Exiting Echoflux OS...")
            break
        else:
            print("Invalid command. Type 'help' for options.")

if __name__ == "__main__":
    main()

