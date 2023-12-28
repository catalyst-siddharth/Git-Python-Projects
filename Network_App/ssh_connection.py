import paramiko
import time
import re


user_file = "S:/Python/Network_App/Credentials.txt"
cmd_file = "S:/Python/Network_App/Configurations.txt"


def ssh_connection(ip):
    
    global user_file
    global cmd_file
    
    try:
        selected_user_file = open(user_file,'r')
        selected_user_file.seek(0)
        
        username = selected_user_file.readlines()[0].split(',')[0]
        #print(username)
        selected_user_file.seek(0)
        password = selected_user_file.readlines()[0].split(',')[1]
        #print(password)
        
        session = paramiko.SSHClient()
        
        session.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        session.connect(ip.rstrip('\n'), username = username, password = password)
        
        connection = session.invoke_shell()
        #connection.send("enable\n")
        connection.send("terminal length 0")
        time.sleep(1)
        
        connection.send("\n")
        #connection.send("configure terminal\n")
        #time.sleep(1)
        
        selected_cmd_file = open(cmd_file, 'r')
        selected_cmd_file.seek(0)
        
        for each_line in selected_cmd_file.readlines():
            connection.send(each_line + "\n")
            time.sleep(2)
            
        selected_cmd_file.close()
        selected_user_file.close()            
      
        router_output = connection.recv(65535)
        
        if re.search(b"% Invalid input", router_output):
            print("There was an input error on the device {} : (".format(ip))
            
        else:
            print("\n+++++++++++++++++++++++++++++++++++++")
            print("Config pushed for device {}".format(ip))
            print("+++++++++++++++++++++++++++++++++++++")
        
        router_text = router_output.decode('UTF-8')
        print(router_text)
        print("\n")
        session.close()
        
    except paramiko.AuthenticationException:
        print("Invalid Username or password")
        print("Closing Program... Bye")