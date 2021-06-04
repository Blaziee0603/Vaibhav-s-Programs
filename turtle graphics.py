

import turtle      

turtle.width(4)
turtle.speed(10)

print("Welcome to the Python sketchbook!")

##### While loop to repeat the main menu

# Initialize the option to empty in order to enter the while loop
option = ""
# Initialize fillcolour to "none" 
f = "none"

while option != "q": # While the option is not "q"
    print()
    print("Please choose one of the following options:")
    print()
    print("m - Move the turtle")
    print("t - Rotate the turtle")
    print("l - Draw a line")
    print("r - Draw a rectangle")
    print("c - Draw a circle")
    print("p - Change the pen colour of the turtle")
    print("f - Change the fill colour of the turtle")
    print("g - Draw a generated flower")
    print("e - Draw an explosion")
    print("a - Draw last two digits of student ID")
    print("q - Quit the program")
    print()

    option = input("Please input your option: ")

    ##### Handle the move option
    if option == "m":
        print()

        # Ask the user for the x and y location
        x = input("Please enter the x location: ")
        x = int(x)
        y = input("Please enter the y location: ")
        y = int(y)

        # Move the turtle without drawing anything
        turtle.up()
        turtle.goto(x, y)
        turtle.down()

    ##### Handle the rotate option
    if option == "t":
        print()

        # Ask user for angle
        angle = input("Please enter the angle by which you want to rotate the turtle: ")
        angle = int(angle)
        # Rotate turtle left
        turtle.left(angle)
        

    ##### Handle the line option
    if option == "l":
        print()

        # Ask the user for the x and y location
        x = input("Please enter the x location: ")
        x = int(x)
        y = input("Please enter the y location: ")
        y = int(y)

        # Move the turtle and draw a line
        turtle.goto(x, y)

    ##### Handle the rectangle option
    if option == "r":
        print()

        # Ask user for height and width
        h = input("Please enter the height of the rectangle: ")
        h = int(h)
        w = input("Please enter the width of the rectangle: ")
        w = int(w)
        # Draw rectangle
        if f != "none":
            turtle.begin_fill()
            turtle.fillcolor(f)
            for _ in range(2):
                turtle.forward(h)
                turtle.left(90)
                turtle.forward(w)
                turtle.left(90)
            turtle.end_fill()
        else:
             for _ in range(2):
                turtle.forward(w)
                turtle.left(90)
                turtle.forward(h)
                turtle.left(90)
                

    ##### Handle the circle option
    if option == "c":
        print()

        # Ask user for radius
        r = input("Please enter the radius of the circle: ")
        r = int(r)
        # Draw circle
        if f != "none":
            turtle.begin_fill()
            turtle.circle(r)
            turtle.end_fill()
        else :
            turtle.circle(r)

    ##### Handle the pen colour option
    if option == "p":
        print()

        # Ask user for pen colour
        c = input("Please enter a colour name: ")
        # Change pen colour
        turtle.pencolor(c)

    ##### Handle the fill colour option
    if option == "f":
        print()

        # Ask user for colour
        f = input("Please enter a colour name (type \"none\" to clear the colour):")
        # Change fill colour
        if f != "none":
            turtle.fillcolor(f)

    #### Handle the generated flower option
    if option == "g":
        print()

        # Ask for radius
        r = input("Please enter the radius of the flower petal: ")
        r = int(r)
        
        # Draw flower
        for _ in range(20):
            for _ in range(4):
                turtle.circle(r, 180)
                turtle.left(90)

            turtle.left(18)

    #### Handle the explosion option
    if option == "e":
        print()

        # Ask user for size
        d = input("Please enter the size of the explosion, it should be greater than or equal to 160: ")
        d = int(d)
        
        # Draw Explosion
        for thiscolor in ["MediumPurple", "OrangeRed","goldenRod", "yellow"]:
            for i in range(4):
                turtle.color(thiscolor + str(i+1))
                turtle.dot(d)
                d = d - 10

    #### Handle the author's name
    if option == "a":
        print()

        turtle.penup()
        turtle.goto(-100,-100)
        turtle.down()
        turtle.circle(50)
        turtle.penup()
        turtle.goto(-100,0)
        turtle.down()
        turtle.circle(50)
        turtle.penup()
        turtle.goto(50,-100)
        turtle.down()
        turtle.circle(50,180)
        turtle.right(90)
        turtle.forward(50)
        turtle.right(90)
        turtle.forward(50)
        
            
turtle.done()
