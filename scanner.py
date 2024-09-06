# Port Scanner
import socket
from colorama import Fore

GREEN =Fore.GREEN
GRAY = Fore.LIGHTBLACK_EX
RESET = Fore.RESET


def portscanner(host, port):
    sock = socket.socket()
    try:
        sock.connect((host, port))
        sock.settimeout(0.2)
    except:
        return False
    else:
        return True


def runner():
    host = input("Please enter host to scan: ")

    for port in range(1, 1000):
        if portscanner(host, port):
            print(f"{GREEN}[+]The port {port} was open on {host}! {RESET}")
        else:
            print(f"{GRAY}[-]Port is closed!{RESET}", end="\r")


if __name__ == "__main__":
    runner()
