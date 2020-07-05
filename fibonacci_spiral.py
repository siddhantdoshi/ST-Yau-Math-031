import turtle
from turtle import Turtle, Screen
import time
import primefac

y = int(input("How many numbers to check: "))
l = []

# for i in range(y):
# 	num = pow(2, i) - 1

# 	if primefac.isprime(num):
# 		# print num
# 		l.append(num)
# 	# else:
# 	# 	l.append(num)

l = primefac.primes(y)

stylePrime = ('Courier', 8, 'bold')
styleNormal = ('Courier', 8)

def plot(k):
	numPrimes = 0
	turtle.pu()
	turtle.hideturtle()
	turtle.speed(0)
	turtle.pencolor("green")
	turtle.write(1, font = stylePrime)
	spacerValue = 20
	#spacerCounter = 10  
	n = 1
	direction = 1

	for i in range(50):
		for j in range(n):
			turtle.setx(turtle.xcor() + spacerValue * direction)
			# if k > spacerCounter:
				# spacerCounter = spacerCounter * 10
				# spacerValue += 15
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
			turtle.sety(turtle.ycor() + spacerValue * direction)
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
		direction = -direction
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

# screen.mainloop()
#___________________________________________________________________________
	   
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