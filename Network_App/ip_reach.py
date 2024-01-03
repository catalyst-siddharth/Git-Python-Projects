from re import findall
from subprocess import Popen, PIPE
import time

def ip_reach(host, ping_count):
    valid_ip = []
    for ip in host:
        data = ""
        output = Popen(f"ping {ip} -n {ping_count}", stdout=PIPE, encoding="utf-8")
        time.sleep(1)
        for line in output.stdout:
            data = data + line
            ping_test = findall("TTL",data)
        if ping_test:
            valid_ip.append(ip)
        else:
            print(f"{ip}: Ping Failed")
    return valid_ip
    