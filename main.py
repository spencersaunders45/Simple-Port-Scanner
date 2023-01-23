import socket
from termcolor import cprint

def scan(target, ports):
    print('\n' + ' Scanning Target ' + str(target))
    for port in range(1,ports+1):
        scan_port(target,port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print(f'{"[+] " + str(port)}{"Open"!s:>9}')
        sock.close()
    except:
        pass

targets = input("[*] Enter targets to scan(separate by comma): ")
ports = int(input("[*] Enter number of ports to scan: "))

if "," in targets:
    cprint("[+] Scanning Multiple Targets",'green')
    for ip in targets.split(','):
        scan(ip.strip(" "), ports)
else:
    scan(targets,ports)

#router ip 192.168.4.1