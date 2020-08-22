import turtle
from turtle import Turtle, Screen
from random import random


import time


 #indices plot
fibPrimesIndices = [3,4,5,7,11,13,17,23,29,43,47,83,131,137,359,431,433,449,509,569,571,2971,4723,5387,9311]
lucPrimesIndices = [0,2,4,5,7,8,11,13,16,17,19,31,37,41,47,53,61,71,79,113,313,353,503,613,617,663,1097]

        


stylePrime = ('Courier', 12, 'bold')
styleNormal = ('Courier', 12)
def plot(k):
    numPrimes = 0
    turtle.pu()
    turtle.hideturtle()
    turtle.speed(10)
    turtle.pencolor("green")
    turtle.write(1, font = stylePrime)
    spacerValue = 38

    #spacerCounter = 10  
    n = 1
    dir = 1
    for i in range(25):
        for j in range(n):
            turtle.setx(turtle.xcor() + spacerValue * dir)
     #       if k > spacerCounter:
      #          spacerCounter = spacerCounter * 10
       #         spacerValue += 15
            if k in fibPrimesIndices and k in lucPrimesIndices:
                
                turtle.pencolor("orange")
                turtle.write(k, font = stylePrime)                

            elif k in fibPrimesIndices:
                
                turtle.pencolor("red")
                turtle.write(k, font = stylePrime)
            elif k in lucPrimesIndices:
                
                turtle.pencolor("pink")
                turtle.write(k, font = stylePrime)                
            else:
                turtle.pencolor("black")
                turtle.write(k, font = styleNormal)
            
            k += 1
        for j in range(n):
            turtle.sety(turtle.ycor() + spacerValue * dir)
            if k in fibPrimesIndices and k in lucPrimesIndices:
                turtle.pencolor("orange")
                turtle.write(k, font = stylePrime)                
            elif k in fibPrimesIndices:                
                turtle.pencolor("red")
                turtle.write(k, font = stylePrime)
            elif k in lucPrimesIndices:
                turtle.pencolor("pink")
                turtle.write(k, font = stylePrime)                            
            else:
                turtle.pencolor("black")
                turtle.write(k, font = styleNormal)
            
            k += 1
        n += 1
        dir =- dir
    # print (k - 1, numPrimes)
    turtle.hideturtle()

plot(2)


#!!!

#!!!!
MAGNIFICATION = 10 # moving using arrow keys

def move_left():
    canvas.xview_scroll(-1, "units")
    turtle.setx(turtle.xcor() - MAGNIFICATION)

def move_right():
    canvas.xview_scroll(1, "units")
    turtle.setx(turtle.xcor() + MAGNIFICATION)

def move_up():
    canvas.yview_scroll(-1, "units")
    turtle.sety(turtle.ycor() + MAGNIFICATION)

def move_down():
    canvas.yview_scroll(1, "units")
    turtle.sety(turtle.ycor() - MAGNIFICATION)

screen = Screen()
width, height = screen.screensize()
screen.screensize(width * MAGNIFICATION, height * MAGNIFICATION)

canvas = screen.getcanvas()
canvas.config(xscrollincrement=str(MAGNIFICATION))
canvas.config(yscrollincrement=str(MAGNIFICATION))


turtle.width(MAGNIFICATION)
turtle.resizemode('auto')


screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.listen()

turtle.mainloop()
