# Prompt users for input
fileChosen = input("Which file to visualize - huskies2016.txt or sampme_data.txt? (recommend the former one) -- ")
title = input("What should the chart be named? -- ")
colorChosen=input("Choose color theme - rainbow or tableau? -- ")

def count_observations(path):
    '''Takes as an argument the path to a file to analyze (a string) and returns the number of observations within that file. This function targets at a particular type of file where each observation takes up 3 lines'''
    with open(path) as f:
        for i, l in enumerate(f):
            pass
    return int((i + 1)/3)

print(count_observations("data/sample_data.txt"))

def observation(lines,n):
    iters = [iter(lines)]*n
    return zip(*iters)
def str_to_num(filename):
    for i in range(len(filename)):
        filename[i]=int(filename[i])
    return filename
def get_max_value(path):
    '''Takes as an argument the path to a file to analyze (a string) and which of the two data features to consider'''
    with open(path) as file:
        groups = zip(*observation(file,3))
        name, feature_1, feature_2 = [sum((g.split() for g in group), []) for group in groups]
        str_to_num(feature_1)
        str_to_num(feature_2)
        return max(feature_1),max(feature_2)

print(get_max_value("data/sample_data.txt"))

# Read the chosen file, and store the respective variables in 3 lists for further drawing. 
file = open('data/'+fileChosen)
groups = zip(*observation(file,3))
name, feature_1, feature_2 = [sum((g.split() for g in group), []) for group in groups]
feature_1 = str_to_num(feature_1)
feature_2 = str_to_num(feature_2)

# Different color palettes that are prompted for useres to choose
def choose_color(colortheme):
    rainbow=['#e41a1c','#377eb8','#4daf4a','#984ea3','#ff7f00','#ffff33']
    tableau=['#74a9cf','#c6dbef','#9ecae1','#6baed6','#3182bd','#08519c']
    return eval(colortheme)

# A module for drawing a chart with the turtle
import turtle  # import module

# Define window size as constants
window = turtle.Screen()  # create a window for the turtle to draw on
window.title(title)  # the title to show at the top of the window
WINDOW_WIDTH = 900  # size constants for easy changing
WINDOW_HEIGHT = 600
window.setup(WINDOW_WIDTH, WINDOW_HEIGHT)  # specify window size (width, height)
window.setworldcoordinates(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)  # coordinate system: origin at lower-left
margin = 30
originx = margin+25
originy = margin
label = 10
height = WINDOW_HEIGHT - margin - originy - label
width = WINDOW_WIDTH - originx - margin
ytick = 5
ymax = max(feature_1)
proportion = ymax/height
spacer = 0.15
unit = len(feature_1)
newfont = ("Arial", 14, "normal")

# Create the turtle
geobugi = turtle.Turtle()
geobugi.speed("fastest")  # how fast the turtle should move

# Move the turtle to draw

def draw_axes(num_of_ticks):
    '''Uses a turtle to draw the axes for the chart, including the tick marks and labels on the x-axis and y-axis. Automatically extract names and values in each file, no other arguments needed. Can take in the argument of how long each tick on y-axis should represent. '''
    geobugi.penup()       # do not draw while moving
    geobugi.goto(originx,originy-label)  # walk to coordinates
    geobugi.pendown()     # start drawing again
    step=width/len(name)
    x=4+originx+step/2+step*spacer*2/len(name)
    geobugi.penup()
    for i in name:
        geobugi.setx(x)
        geobugi.write(i,True,align='center',font=newfont)
        x=x+step
    geobugi.goto(originx,originy+label)
    geobugi.pendown()
    geobugi.left(90)
    per_tick = ymax/num_of_ticks
    ave = height/(num_of_ticks)
    for i in range(0,num_of_ticks):
        geobugi.forward(ave)
        geobugi.left(90)
        geobugi.forward(ytick)
        geobugi.penup()
        geobugi.forward(30)
        geobugi.write(round((i+1)*per_tick,1),font=newfont)
        geobugi.right(180)
        geobugi.forward(30+ytick)
        geobugi.pendown()
        geobugi.left(90)
    geobugi.goto(originx,originy+label)
    geobugi.pendown()
    geobugi.right(90)
    geobugi.forward(width+width/unit*spacer)

draw_axes(10)

def draw_rectangle(t, height, color):
    """ Get turtle t to draw one bar, of height. Takes in the arguments of turtle, height (to be extracted from a list), and color. """
    t.begin_fill()               # start filling the rectangle
    t.color(color)
    t.penup()
    t.forward(width/unit*spacer)    # space between rectangles
    t.pendown()
    t.left(90)
    t.forward(height/proportion)    # adjust difference between the numerical value of an item and the height on graph
    t.right(90)
    t.forward(width/unit*(1-spacer))    # width of each rectangle
    t.right(90)
    t.forward(height/proportion)
    t.left(90)
    t.end_fill()                 # stop filling the rectangle

def draw_bars(color):
    '''Uses a turtle to draw all the bars for the chart on the screen. Takes in the argument of color, which is prompted to the user in the beginning.'''
    geobugi.goto(originx,originy+label)
    count=0
    for i in feature_1:
        draw_rectangle(geobugi, i, color[count])
        count += 1
        if(count >= len(color)):
            count = 0
        i += 1
    geobugi.penup()
    geobugi.goto(originx,originy+label)


draw_bars(choose_color(colorChosen))

# Make the turtle graphics appear and run, waiting for the user to close the screen
# This MUST be the last statement executed in the script
window.mainloop()