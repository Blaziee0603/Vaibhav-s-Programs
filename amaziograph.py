

import turtle

turtle.setup(800,600)    # Set the width and height be 800 x 600

number_of_divisions = 8  # The number of subdivisions around the centre
turtle_width = 3         # The width of the turtles

# Don't show the animation
turtle.tracer(False)

# Draw the background lines

backgroundTurtle = turtle.Turtle()

backgroundTurtle.width(1)

backgroundTurtle.down()
backgroundTurtle.color("gray88") # Draw the centered line
for i in range(number_of_divisions):
    backgroundTurtle.forward(500)
    backgroundTurtle.backward(500)
    backgroundTurtle.left(360 / number_of_divisions)

backgroundTurtle.up()

# Show the instructions
backgroundTurtle.color("purple")
backgroundTurtle.goto(-turtle.window_width()/2+50, 100)
backgroundTurtle.write("""s - change a colour for one of the colour buttons
m - all 8 drawing turtles go to middle
c - clear all drawings made by the 8 drawing turtles
""", font=("Arial", 14, "normal"))

backgroundTurtle.hideturtle()

# Set up a turtle for handling message on the turtle screen
messageTurtle = turtle.Turtle()
# This sets the colour of the text to red
messageTurtle.color("red")
# We do not want it to show/draw anything, except the message text
messageTurtle.up() 
# Set it the be at center, near the colour selections
messageTurtle.goto(0, -200)
# We do not want to show it on the screen
messageTurtle.hideturtle()

# Part 2 Preparing the drawing turtles

# The drawing turtles are put in a list
allDrawingTurtles = [] 

# Part 2.1 Add the 8 turtles in the list
for _ in range(number_of_divisions):
    temp = turtle.Turtle()
    temp.speed(0)
    temp.width(turtle_width)
    temp.hideturtle()
    allDrawingTurtles.append(temp)
    
# Part 2.2 Set up the first turtle for drawing
dragTurtle = allDrawingTurtles[0]
dragTurtle.shape("circle")
dragTurtle.shapesize(2)
dragTurtle.showturtle()

# Part 3 Preparing the basic drawing system
def draw(x, y):
    dragTurtle.ondrag(None)
    turtle.tracer(False)
    messageTurtle.clear()
    dragTurtle.goto(x, y)
    x_transform = [1, 1, -1, -1, 1, 1, -1, -1] # This represents + + - - + + - -
    y_transform = [1, -1, 1, -1, 1, -1, 1, -1] # This represents + - + - + - + -

    for i in range(1, number_of_divisions):
        if i < 4:
            new_x = x * x_transform[i] # x with sign change
            new_y = y * y_transform[i] # y with sign change
    	
        else:
            new_x = y * y_transform[i] # Note that we assign y as new x
            new_y = x * x_transform[i] # Note that we assign x as new y
        allDrawingTurtles[i].goto(new_x, new_y)
    turtle.tracer(True)
    dragTurtle.ondrag(draw)
dragTurtle.ondrag(draw)

# Part 5.2 clear all drawings made by the 8 drawing turtles
def clearDrawing():
    for c in allDrawingTurtles:
        c.clear()
    messageTurtle.clear()
    messageTurtle.write("The screen is cleared", \
                       align="center", font=("Arial", 14, "normal"))
turtle.onkeypress(clearDrawing, 'c')


# Part 5.3 all 8 drawing turtles go to middle
def goToMiddle():
    for c in allDrawingTurtles:
        c.up()
        c.goto(0, 0)
        c.down()
    messageTurtle.clear()
    messageTurtle.write("All 8 turtles returned to the middle", \
                       align="center", font=("Arial", 14, "normal"))
turtle.onkeypress(goToMiddle, 'm')


# Part 4 handling the colour selection
# Here is the list of colours
colours = ["black", "orange red", "lawn green", "medium purple", "light sky blue", "orchid", "gold"]

# Part 4.2 Set up the onclick event
def handleColourChange(x, y):
    if x <= -130:
        for m in range(len(allDrawingTurtles)):
            allDrawingTurtles[m].color(colours[0])
    elif x <= -80:
        for m in range(len(allDrawingTurtles)):
            allDrawingTurtles[m].color(colours[1])
    elif x <= -20:
         for m in range(len(allDrawingTurtles)):
            allDrawingTurtles[m].color(colours[2])
    elif x <= 30:
         for m in range(len(allDrawingTurtles)):
            allDrawingTurtles[m].color(colours[3])
    elif x <= 80:
         for m in range(len(allDrawingTurtles)):
            allDrawingTurtles[m].color(colours[4])
    elif x <= 130:
         for m in range(len(allDrawingTurtles)):
            allDrawingTurtles[m].color(colours[5])
    elif x <= 180:
         for m in range(len(allDrawingTurtles)):
            allDrawingTurtles[m].color(colours[6])


# Part 5.4 change a colour in the colour selection
def changeColour():
    index  = turtle.textinput( \
                "Change colour", \
                "Please enter the index number for the turtle(0-6)")
    
    if index != None:
        while (int(index)<0 or int(index)>6):
            messageTurtle.clear()
            messageTurtle.write("Wrong Input", \
                       align="center", font=("Arial", 14, "normal"))
            index  = turtle.textinput( \
                "Change colour", \
                "Please enter the index number for the turtle(0-6)")
            
        col = turtle.textinput( \
                "Change colour", \
                "Please enter the colour you want to use")
        if col != None:
            colours[int(index)] = col
            colourSelectionTurtles[int(index)].color(col)
            messageTurtle.clear()
            messageTurtle.write("The colour is set and can be used", \
                       align="center", font=("Arial", 14, "normal"))
    turtle.listen()
turtle.onkeypress(changeColour, 's')


# Part 4.1 Make the colour selection turtles
colourSelectionTurtles = []
for i in range(len(colours)):
    temp = turtle.Turtle()
    temp.color(colours[i])
    temp.shape("square")
    temp.shapesize(2, 2)
    temp.up()
    temp.goto(-150 + (i*50), -250)
    temp.down()
    temp.onclick(handleColourChange)
    colourSelectionTurtles.append(temp)


turtle.tracer(True)
turtle.listen()

turtle.done()

