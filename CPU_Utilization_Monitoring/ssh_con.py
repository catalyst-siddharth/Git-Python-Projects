import paramiko
import time
import re
from datetime import datetime

user_file = "S:/Git-Python-Projects/CPU_Utilization_Monitoring/credentials.txt"
cmd_file = "S:/Git-Python-Projects/CPU_Utilization_Monitoring/configurations.txt"

def ssh_con(ip):
    global user_file
    global cmd_file
    
    try:
        selected_user_file = open(user_file,'r')
        selected_cmd_file = open(cmd_file,'r')
        now = datetime.now()
        current_time = now.strftime("%Y-%m-%d %H:%M:%S")
        
        username = selected_user_file.readlines()[0].split(',')[0]
        selected_user_file.seek(0)
        password = selected_user_file.readlines()[0].split(',')[1]
            
        session = paramiko.SSHClient()
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        session.connect(ip.rstrip("\n"), username=username, password=password)
        connection = session.invoke_shell()
        
        connection.send("terminal length 0")
        time.sleep(1)
        connection.send("\n")
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line+"\n")
            time.sleep(1)
            
        router_output = connection.recv(65535)
        if re.search(b"% Invalid input", router_output):
            print(f"Input Error Detected on device {ip} ")
        else:
            print(f"{current_time}: CPU Utilization pushed for the device {ip}")
        cpu = re.search(b"one(\s)minute:(.+?)%",router_output)
        utilization = cpu.group(2).decode("utf-8")
        
        with open("S:/Git-Python-Projects/CPU_Utilization_Monitoring/cpu.txt","a") as f:
            f.write(utilization+"\n")
        
        session.close()
        selected_user_file.close()
        selected_cmd_file.close()
        
    except paramiko.AuthenticationException:
        print("Invalid Username or Password. Closing Connection. Bye !")