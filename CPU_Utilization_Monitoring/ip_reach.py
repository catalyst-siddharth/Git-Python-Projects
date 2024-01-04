from subprocess import Popen, PIPE
from re import findall
import sys


ip_address_file = "S:/Git-Python-Projects/CPU_Utilization_Monitoring/ip_address.txt"

def all_ip():
    selected_ip_file = open(ip_address_file,'r')
    ip_address_list = []
    for ip in selected_ip_file:
        trim_ip = ip.strip()
        ip_address_list.append(trim_ip)
        
    selected_ip_file.close()
    return ip_address_list

inventory = all_ip()

def valid_ip():
    global inventory
    valid_ip = []
    for ip in inventory:
        data = ""
        output = Popen(f"ping {ip} -n 1", stdout=PIPE, encoding="utf-8")
        for line in output.stdout:
            data = data + line
            ping_test = findall("TTL",data)
        if ping_test:
            valid_ip.append(ip)
    
    if not valid_ip:
        print("\n\nNone of the IP's are pingnig.. Exiting.!!\n")
        sys.exit()
    else:          
        return valid_ip


def failed_ip():
    global inventory
    failed_ip = []
    for ip in inventory:
        data = ""
        output = Popen(f"ping {ip} -n 1", stdout=PIPE, encoding="utf-8")
        for line in output.stdout:
            data = data+line
            ping_test = findall("TTL",data)
        if not ping_test:
            failed_ip.append(ip)
            
        return failed_ip