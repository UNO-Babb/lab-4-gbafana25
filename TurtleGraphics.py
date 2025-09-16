#TurtleGraphics.py
#Name: Gareth Moodley 
#Date: 9-16-2025
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
#hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(myTurtle, sides):
    # num of sides should dictate angle 
    turn_angle = (180*(sides-2))//sides
    for i in range(sides):
        myTurtle.forward(50)
        myTurtle.right(turn_angle-180)

def fillCorner(myTurtle, quadrant):
    drawSquare(myTurtle, 100)
    myTurtle.up()
    if quadrant == 2:
        myTurtle.forward(50)
        myTurtle.down()
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    elif quadrant == 3:
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.left(90)
        myTurtle.down()
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    elif quadrant == 4:
        myTurtle.right(90)
        myTurtle.forward(50)
        myTurtle.left(90)
        myTurtle.forward(50)
        myTurtle.down()
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()
    else:
        myTurtle.down()
        myTurtle.begin_fill()
        drawSquare(myTurtle, 50)
        myTurtle.end_fill()


def squaresInSquares(myTurtle, num):
    size = 100
    for i in range(num):
        drawSquare(myTurtle, size)
        size -= 20
        myTurtle.up()
        myTurtle.forward(10)
        myTurtle.right(90)
        myTurtle.forward(10)
        myTurtle.left(90)
        myTurtle.down()

def main():
    myTurtle = turtle.Turtle()
    drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon

    fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
