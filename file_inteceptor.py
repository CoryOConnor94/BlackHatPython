import scapy.all as scapy
import netfilterqueue

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet())   # Bind to queue created
queue.run()

def process_packet(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # print(scapy_packet.show())    # Testing
    if scapy_packet.haslayer(scapy.Raw):
        if scapy_packet[scapy.TCP].dport == 80:
            print('This is a HTTP Request')
            print(scapy_packet.show())
        elif scapy_packet[scapy.TCP].sport == 80:
            print('This is a HTTP Response')
            print(scapy_packet.show())

    packet.accept()
