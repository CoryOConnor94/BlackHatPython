#!/usr/bin/env python3
import scapy.all as scapy
from scapy.layers.l2 import ARP, Ether, srp
import argparse


def get_arguments():
    """
    Parses command line arguments, defines expected arguments, and returns them

    :return: Parsed command line arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='IP/IP range to scan')
    options = parser.parse_args()
    if not options.target:
        parser.error('[+] Please specify an IP or range of IPs to scan, use --help for more info')
    return options


def discovery_scan(ip):
    """
    Performs network discovery scan by creating arp request, appending to ethernet frame and broadcasting
    :param ip: Given IP/Range from command line
    :return: List of responded devices IP and MAC addresses
    """
    arp_request = ARP(pdst=ip)  # Create ARP request to ask who has given IP
    broadcast = Ether(dst='ff:ff:ff:ff:ff:ff')  # Create Ethernet frame and Set destination MAC to broadcast MAC
    arp_request_broadcast = broadcast/arp_request   # Append ARP request to Ethernet frame

    # Send packet and receive answered and unanswered responses
    answered_list = srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    results_list = []
    for element in answered_list:
        results_list.append({'IP': element[1].psrc, 'MAC': element[1].hwsrc})

    return results_list


def print_results(results):
    """
    Displays results of ARP discovery scan
    :param results: List of responded devices IP and MAC addresses
    """
    for client in results:
        print(f'[+]IP = {client["IP"]}\n[+]MAC = {client["MAC"]}')
        print('------------------------------------------------')


def main():
    """
    Main flow of program:
    Parses command line arguments, runs arp discovery scan, prints response IP and MAC addresses
    """
    options = get_arguments()
    discovery_results = discovery_scan(options.target)
    print_results(discovery_results)


if __name__ == '__main__':
    main()


