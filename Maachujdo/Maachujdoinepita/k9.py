#!/usr/bin/python3
# by nu11secur1ty
import snifhttp
import colorama
from colorama import Fore, Style

iface = input(Fore.GREEN + "Type the sniffing interface\n")
try:
    snifhttp.sniffing(Fore.YELLOW + iface)
 
except KeyboardInterrupt:
    print('Exit...')
