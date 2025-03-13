#!/usr/bin/env python
import subprocess
import argparse
import re


def get_arguments():
    """
      Parses command line arguments, defines expected arguments, and returns them

      :return: Parsed command line arguments (interface, new mac address)
      """
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', dest='interface', help='interface to change its MAC address')
    parser.add_argument('-m', '--mac', dest='new_mac', help='New MAC address')
    options = parser.parse_args()
    if not options.interface:
        parser.error('[+] Please specify an interface, use --help for more info')
    elif not options.new_mac:
        parser.error('[+] Please specify a new MAC address, use --help for more info')
    return options


def get_current_mac(interface):
    """
    Retrieves MAC address of given interface by running ifconfig command and uses regex pattern to extract MAC
    :param interface: Given interface from command line
    :return: Mac address of interface
    """
    ifconfig_result = subprocess.check_output(['ifconfig', interface])
    current_mac_address = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', str(ifconfig_result))
    if current_mac_address:
        return current_mac_address.group(0)
    else:
        print('Could not read MAC address of given interface')


def change_mac(interface, new_mac):
    """
    Changes MAC address by using ifconfig commands
    :param interface: Given interface from command line
    :param new_mac: MAC address of interface
    """
    print('[+] Changing MAC address for ' + interface + ' to ' + new_mac)
    #
    # subprocess.call(['ifconfig', interface, 'down'])
    # subprocess.call(['ifconfig', interface, 'hw', 'ether', new_mac])
    # subprocess.call(['ifconfig', interface, 'up'])


def main():
    """
    Main flow of program:
    Parses command line arguments, gets MAC address of given interface, changes to given new MAC address
    :return:
    """
    options = get_arguments()
    # change_mac(options.interface, options.new_mac)
    current_mac = get_current_mac(options.interface)
    if current_mac != options.new_mac:
        change_mac(options.interface, options.new_mac)


if __name__ == '__main__':
    main()
