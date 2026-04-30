import numpy as np
from letters import letter


def draw_ellipse(a,b,xi,yi):
    t = 0  
    dt = (np.pi)/100
    dx = 0
    dy = 0
    commands = []
    commands.append("G90")
    while t<=2*(np.pi):
        x = (-a)*np.cos(t) + a
        y = b*np.sin(t)
        yf = yi - y
        xf = xi + x
        commands.append(f"G1 X{xf:.10f} Y{yf:.10f} F500")
        t += dt
    commands.append("G91")
    return commands




        

