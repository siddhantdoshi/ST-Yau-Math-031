import turtle
from turtle import Turtle, Screen
from random import random


import time

# y = int(input("How many powers of 2 to check:"))
l = [3, 4, 5, 7, 11, 13, 17, 23, 29, 43, 47, 83, 131, 137,
 359, 431, 433, 449, 509, 569, 571, 2971, 4723, 5387, 9311, 9677,
  14431, 25561, 30757, 35999, 37511, 50833, 81839, 104911, 130021,
   148091, 201107, 397379, 433781, 590041, 593689, 604711, 931517,
    1049897, 1285607, 1636007, 1803059, 1968721, 2904353, 3244369, 3340367]
#
# for i in range(y):
#     num = pow(2,i) - 1
#     if num > 1:
#        for j in range(2,num):
#            if (num % j) == 0:
#                break
#        else:
#            l.append(num)




stylePrime = ('Courier', 15, 'bold')
styleNormal = ('Courier', 15)
def plot(k):
    numPrimes = 0
    turtle.pu()
    turtle.hideturtle()
    turtle.speed(10)
    turtle.pencolor("green")
    turtle.write(1, font = stylePrime)
    spacerValue = 45
    #spacerCounter = 10
    n = 1
    dir = 1
    for i in range(20):
        for j in range(n):
            turtle.setx(turtle.xcor() + spacerValue * dir)
     #       if k > spacerCounter:
      #          spacerCounter = spacerCounter * 10
       #         spacerValue += 15
            if k in l:
            # if isPrime(k):
                # print(k)
                numPrimes += 1
                turtle.pencolor("red")
                turtle.write(k, font = stylePrime)
            else:
                turtle.pencolor("black")
                turtle.write(k, font = styleNormal)

            k += 1
        for j in range(n):
            turtle.sety(turtle.ycor() + spacerValue * dir)
            # if isPrime(k):
            if k in l:
                # print(k)
                numPrimes += 1
                turtle.pencolor("red")
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
MAGNIFICATION = 10

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
#_________________________

"""3, 4, 5, 7, 11, 13, 17, 23, 29, 43, 47, 83, 131, 137,
 359, 431, 433, 449, 509, 569, 571, 2971, 4723, 5387, 9311, 9677,
  14431, 25561, 30757, 35999, 37511, 50833, 81839, 104911, 130021,
   148091, 201107, 397379, 433781, 590041, 593689, 604711, 931517,
    1049897, 1285607, 1636007, 1803059, 1968721, 2904353, 3244369, 3340367"""

"""def isPrime(n) :

    # Corner cases
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True"""
