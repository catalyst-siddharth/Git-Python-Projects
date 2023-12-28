import sys

from ip_file_valid import ip_file_valid
from ip_addr_valid import ip_addr_valid
from ip_reach import ip_reach
from ssh_connection import ssh_connection
from create_threads import create_threads
from log_file import log_file

ip_list = ip_file_valid()

try:
    ip_addr_valid(ip_list)
except KeyboardInterrupt:
    print("\n\nProgram Interrupted by User. Exiting ... \n")
    sys.exit()
    

try:
    ip_reach(ip_list,1)
except KeyboardInterrupt:
    print("\n\nProgram Interrupted by User. Exiting ... \n")
    sys.exit()
    

for ip in ip_list:
    create_threads(ip_list, ssh_connection(ip))
    log_file(ip)