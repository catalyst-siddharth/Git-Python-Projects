import os.path
import sys

def ip_file_valid():
    file_path = "S:/Git-Python-Projects/Network_App/IP_Address.txt"
    file_exist = os.path.exists(file_path)
    
    #Checking if file exists:
    ip_list = []
    if file_exist:
        #print("\nThe file exists !!! Find the contents of file below: \n\n")
        open_file = open(file_path,'r')
        for ip in open_file.read().splitlines():
            ip_list.append(ip)
    else:
        print("\nFile doesn't exist. Please check and try again.\n\n")
        sys.exit()
        
    open_file.close()
    #print(ip_list)
    return ip_list
        
            
