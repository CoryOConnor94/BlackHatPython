#!/usr/bin/env python
from asyncio import timeout

import scapy.all as scapy
from scapy.layers.l2 import ARP, Ether

def scan(ip):
    arp_request = ARP(pdst=ip)  # Create ARP request to ask for given IP
    # print(arp_request.summary())
    arp_request.show()
    broadcast = Ether(dst='ff:ff:ff:ff:ff:ff')  # Set destination MAC to broadcast MAC
    # scapy.ls(Ether())
    broadcast.show()
    arp_request_broadcast = broadcast/arp_request   # Combine packets
    arp_request_broadcast.show()
    answered_list, unanswered_list = scapy.srp(arp_request_broadcast, timeout=1)    # Send packet and receive answered and unanswered responses
    print(answered_list.summary())
    print(unanswered_list.summary())





scan('192.168.0.1/24')


