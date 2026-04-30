from letters import letter
from ellipse_maker_copy import draw_ellipse


file_name = "hello.gcode"
full_file_name = rf"project\g_codefolder\{file_name}"
#everything under is supposed to be in millimeters
initial = [0,0] #initial x,y
iteration = 0 #nth letter or space or whatever
spacing = 1 #spacing between letters in mm
tx_length = 0 #x position
ty_length = 0 #y position
x_size = 180 #size of the paper or wherever the machine can reach in x direction
g_code = []

decimals = 2 # rounding decimal 
#word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
word = "I LOVE APPLES"

def generate_gcode(single, size=1):
    global g_code, iteration, tx_length, ty_length

    l_space_scale = round((spacing*size),decimals) #scaled spacing between letters
    xlength = 0 # length of letter with letter spacing in x direction
    ylength = 0 #height of letter

    if iteration == 0: # checks if it's the first letter to see where to start
        g_code.append("G90")
        g_code.append(f"G21")
        g_code.append(f"G1 Z10 F500")
        g_code.append(f"G1 X{initial[0]} Y{initial[1]} F1500")
        g_code.append("G91")


    for step in letter[single]:
        cmd = step[0] #checks the command that the letter requires

        if cmd == "line":
            x = round((step[1] * size), decimals)
            y = round((step[2] * size), decimals)

            g_code.append(f"G1 X{x} Y{y} F1500")

            xlength += x
            ylength += y

        elif cmd == "down":
            g_code.append("G1 Z-10 F500")

        elif cmd == "up":
            g_code.append("G1 Z10 F500")

        elif cmd == "cw" or cmd == "ccw":# arc drawing
            w = "" #clock wiseness
            x = round((step[1] * size),decimals)
            y = round((step[2] * size), decimals)
            i = round((step [3] * size),decimals)
            j = round((step [4] * size), decimals)
            if cmd == "cw":#clockwise
                w = "G02"
            else: w = "G03"
            g_code.append(f"{w} X{x} Y{y} I{i} J{j} ")

            xlength += x
            ylength += y

        elif cmd == "ellipse":
            a = step[1] #horizontal radius
            b = step[2] #vertical radius
            d = step[3] #side to draw on

            if d == "l":#draw on left
                a *= -1
        
            for i in draw_ellipse(a,b,tx_length+xlength ,ty_length+ylength): 

                g_code.append(i)
        

    tx_length += xlength + l_space_scale #adds to total xlength
    ty_length += ylength


    g_code.append(f"G1 X{l_space_scale} Y0 F1500")
    iteration += 1




def save_gcode(full_file_name, lines):
    with open(full_file_name, "w") as f:
        f.write(lines)


for i in word:
     generate_gcode(i)

fg_code = ""
for i in g_code:
    fg_code = fg_code + f"{i}\n"
save_gcode(full_file_name, fg_code )
