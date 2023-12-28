from datetime import datetime

cmd_file = "S:/Python/Network_App/Configurations.txt"

def log_file(ip):
    global cmd_file
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    selected_file = open(cmd_file,'r')
    app_log_file = open("logs.txt",'a')
        
    for each_line in selected_file.readlines():
        app_log_file.write(f"{current_time} {ip}\t{each_line}")
    
    #app_log_file.write("\n")
            
    selected_file.close()
    app_log_file.close()
    