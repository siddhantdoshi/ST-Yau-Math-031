import turtle
from turtle import Turtle, Screen
from random import random


import time

fibonacci_prime_indices = [3, 4, 5,7,11,13,17,23,29,43,47,83,131,137,359,431,433,449,509,569,571,2971,4723,5387,9311,9677,14431,25561,30757,
35999,37511,50833,81839,104911,130021,148091,201107,397379,433781,590041,593689,604711,931517,1049897,1285607,1636007,1803059,
1968721,2904353,3244369,3340367]
lucas_prime_indices = [2,4,5,7,8,11,13,16,17,19,31,37,41,47,53,61,71,79,113,313,353,503,613,617,863,1097,1361,4787,4793,5851,7741,8467,10691,
12251,13963,14449,19469,35449,36779,44507,51169,56003,81671,89849,94823,140057,148091,159521,183089,193201,202667,344293,
387433,443609,532277,574219,616787,631181,637751,651821,692147,901657,1051849]


stylePrime = ('Courier', 15, 'bold')
styleNormal = ('Courier', 15)

# defining the beginning of the ulam spiral
def plot(k):
    numPrimes = 0
    turtle.pu()
    turtle.hideturtle()
    turtle.speed(10)
    turtle.pencolor("red")
    turtle.write(1, font = stylePrime)
    spacerValue = 45
    n = 1
    dir = 1
    for i in range(40):
        for j in range(n):
            turtle.setx(turtle.xcor() + spacerValue * dir)

# setting the colours and fonts of the fibonacci_prime_indices and the lucas_prime_indices
            if k in fibonacci_prime_indices and k in lucas_prime_indices:
                numPrimes += 1
                turtle.pencolor("orange")
                turtle.write(k, font = stylePrime)
            elif k in lucas_prime_indices:
                numPrimes += 1
                turtle.pencolor("red")
                turtle.write(k, font = stylePrime)
            elif k in fibonacci_prime_indices:
                numPrimes += 1
                turtle.pencolor("green")
                turtle.write(k, font = stylePrime)
            else:
                turtle.pencolor("black")
                turtle.write(k, font = styleNormal)

            k += 1
        for j in range(n):
            turtle.sety(turtle.ycor() + spacerValue * dir)
            if k in fibonacci_prime_indices and k in lucas_prime_indices:
                numPrimes += 1
                turtle.pencolor("orange")
                turtle.write(k, font = stylePrime)
            elif k in lucas_prime_indices:
                numPrimes += 1
                turtle.pencolor("red")
                turtle.write(k, font = stylePrime)
            elif k in fibonacci_prime_indices:
                numPrimes += 1
                turtle.pencolor("green")
                turtle.write(k, font = stylePrime)
            else:
                turtle.pencolor("black")
                turtle.write(k, font = styleNormal)

            k += 1
        n += 1
        dir =- dir
    turtle.hideturtle()

plot(2)
MAGNIFICATION = 10

# allows you to scroll to see the ulam spiral

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

screen.mainloop()
