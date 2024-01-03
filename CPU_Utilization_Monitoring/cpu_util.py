from ip_reach import valid_ip
from ssh_con import ssh_con
from create_threads import create_threads
import sys
import time

ip_list = valid_ip()

try:
    valid_ip()
    
except:
    print("\n\nProgram aborted by the user. Exiting ...\n")
    sys.exit()

while True:
    create_threads(ip_list, ssh_con)
    time.sleep(10)