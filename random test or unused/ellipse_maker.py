import numpy as np
from letters import letter


def draw_ellipse(a,b):  
    dx = 0.01/b
    dx_total = -a #distance from -a
    iteration = 0 #building top half
    y_prev = 0 #previous y
    commands = []
    while True:
        if dx_total >= a: #checks if going outside of domain
            if iteration == 0: #resets to make bottom half
                iteration = 1
                dx_total = -a
                y_prev = 0
                break
            else: #bottom half has been made, ellipse complete
                break
    
        y = b*np.sqrt(1-np.power(dx_total/a, 2))
        dy = y - y_prev

        if iteration == 1: #checks y displacement
            commands.append(f"G1 X{-dx:.10f} Y{-dy:.10f} F500")
        else:
            commands.append(f"G1 X{dx:.10f} Y{dy:.10f} F500")

        dx_total += dx
        y_prev = y
    return commands




        

