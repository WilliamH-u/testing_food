from letters import letter, max_height
from ellipse_maker_copy import draw_ellipse
import sys

file_name = "hello.gcode"
full_file_name = rf"project\g_codefolder\{file_name}"
#everything under is supposed to be in millimeters
initial = [20,-20] #initial x,y
size = 0.5 #multiplier for size, default size is max_height being the max height
iteration = 0 #nth letter or space or whatever
spacingx = 1 #spacing between letters in mm in x direction
spacingy = 2 #spacing between letters in mm in y direction
tx_length = initial[0] #x position
ty_length = initial[1] #y position
cx_length = 0 #tx_length + length of the next letters until the next space, so adds length of next word or remainder of a word to the current position for checking if it will fit
x_size = 180 #size of the paper or wherever the machine can reach in x direction
g_code = []
mode = "skip" #2 modes of operation:
#"skip" means write the full word in the next line when you get to the end of the x axis space
#"continue" means write continue writing each letter until no more space on x axis then next line, so the word will just get cut off

decimals = 10 # rounding decimal 
#current limitations for what it can write: only capital alphabet letters and space
#word = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
word = "I LOVE APPLES AND BIG FAT HAMBURGERS WITH FRIES ON THE SIDE"

def generate_gcode(single,index=0, checker = False):
    global g_code, iteration, tx_length, ty_length,cx_length

    if single == " ":#to not add extra space
            l_space_scale = 0 
    else:
        l_space_scale = round((spacingx*size),decimals) #scaled spacing between letters

    y_space_scale = round((spacingy*size),decimals) #scaled spacing between letters
    max_height_scale = round((max_height*size),decimals)

    xlength = 0 # length of letter with letter spacing in x direction
    ylength = 0 #height of letter
    if checker == False:
        cx_length = tx_length

        if iteration == 0: # checks if it's the first letter to see where to start
            g_code.append("G90")
            g_code.append(f"G21")
            g_code.append(f"G1 Z10 F500")
            g_code.append(f"G1 X{initial[0]} Y{initial[1]} F1500")
            g_code.append("G91")

        if mode == "skip":
            for i in word[index:]: #adds length of next word or remaining length of a word to the current position to check if it will fit in given area
                if i == " ":
                    break
                generate_gcode(i, checker = True)

        elif mode == "continue":
            generate_gcode(single, checker = True)
        
        if cx_length >= x_size: #checking to see if it fits
            if (cx_length+initial[0]-tx_length) >= x_size:#checks if whatever will fit given indentation and size of letter or word if new line started
                print("Does not fit in current configuration")
                sys.exit()

            g_code.append(f"G1 X{-tx_length+initial[0]} Y{-(y_space_scale+max_height_scale)} F1500")
            tx_length = initial[0]#reframing
            ty_length = initial[1] - (y_space_scale+max_height_scale)


    for step in letter[single]:
        cmd = step[0] #checks the command that the letter requires

        if cmd == "line":
            x = round((step[1] * size), decimals)
            y = round((step[2] * size), decimals)
            if checker == False:
                g_code.append(f"G1 X{x} Y{y} F1500")

            xlength += x
            ylength += y
        
        
        elif cmd == "down":
            if checker == False:
                g_code.append("G1 Z-10 F500")

        elif cmd == "up":
            if checker == False:
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

            if checker == False:
                g_code.append(f"{w} X{x} Y{y} I{i} J{j} ")

            xlength += x
            ylength += y

        elif cmd == "ellipse" and checker == False: # LENGTH CHECKER WONT WORK WITH ELLIPSES, IT WONT SKIP A LINE, NO POINT TO HAVE RIGHT NOW
            a = step[1] #horizontal radius
            b = step[2] #vertical radius
            d = step[3] #side to draw on

            if d == "l":#draw on left
                a *= -1
        
            for i in draw_ellipse(a,b,tx_length+xlength ,ty_length+ylength): 
                g_code.append(i)
        
    if checker == False:
        tx_length += xlength + l_space_scale #adds to total xlength
        ty_length += ylength
        if l_space_scale!=0:
            g_code.append(f"G1 X{l_space_scale} Y0 F1500")
        iteration += 1

    
    if checker == True:
        cx_length += xlength + l_space_scale


def save_gcode(full_file_name, lines):
    with open(full_file_name, "w") as f:
        f.write(lines)


for i, l in enumerate(word): #generate g code
     generate_gcode(l, i)

fg_code = ""
for i in g_code:
    fg_code = fg_code + f"{i}\n"
save_gcode(full_file_name, fg_code )
