from re import findall
from subprocess import Popen, PIPE
from ip_file_valid import ip_file_valid
import sys

def ip_reach(host, ping_count):
    for ip in host:
        data = ""
        output = Popen(f"ping {ip} -n {ping_count}", stdout=PIPE, encoding="utf-8")
        for line in output.stdout:
            #print(line)
            data = data + line
            #print(data)
            ping_test = findall("TTL",data)
        if not ping_test:
            print(f"{ip}: Failed Ping")
        
        sys.exit(0)
                   
                
nodes = ip_file_valid()
ip_reach(nodes,1)
    