import re
from ip_file_valid import ip_file_valid

def ip_addr_valid(ip_address):
    ip_address = ip_file_valid()
    ip_validity = []
    for ip in ip_address:
        class_a = re.search(r"[10].[0-255].[0-255].[0-255]",ip)
        class_b = re.findall(r"[172].1[6-9]|2[0-9]|3[0-1].[0-255].[0-255]",ip)
        class_c = re.search(r"[192].[168].[0-255].[0-255]",ip)
        if class_a or class_b or class_c:
            #print("\nValid IP Address...\n\n")
            ip_validity.append(True)
    if True in ip_validity:
        return True
    else:
        return False
        
