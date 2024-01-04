import matplotlib.pyplot as pyp
import matplotlib.animation as animation
import os.path
import sys

figure = pyp.figure()

subplot = figure.add_subplot(1,1,1)

graph_file = "S:/Git-Python-Projects/CPU_Utilization_Monitoring/Data/"
selected_graph_file = input("\n\nEnter the ip address for which you want to see the graph: ")
file_name = str(graph_file+selected_graph_file+".txt")
file_exist = os.path.exists(file_name)

def animation_function(i):
    if file_exist:
        open_file = open(file_name)
    else:
        print("\n\nFile does not exist. Please check and try again.")
        sys.exit()
    
    cpu_data = open_file.readlines()
    x = []
    for each_value in cpu_data:
        if len(each_value)>1:
            x.append(float(each_value))
            
    subplot.clear()
    subplot.plot(x)
    
if animation_function:
    graph_animation = animation.FuncAnimation(figure, animation_function, interval = 10000)
    pyp.show()
else:
    print("\n\nFile name was not Found. Exiting ... ")