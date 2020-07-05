import turtle

l = [3, 4, 5, 7, 11, 13, 17, 23, 29, 43, 47, 83, 131, 137,
 359, 431, 433, 449, 509, 569, 571, 2971, 4723, 5387, 9311, 9677,
  14431, 25561, 30757, 35999, 37511, 50833, 81839, 104911, 130021,
   148091, 201107, 397379, 433781, 590041, 593689, 604711, 931517,
    1049897, 1285607, 1636007, 1803059, 1968721, 2904353, 3244369, 3340367]

def isPrime(n) :

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

    return True

def plot(k):
    numPrimes = 0
    turtle.pu()
    turtle.speed(0)
    turtle.pencolor("green")
    turtle.dot(5)
    n = 1
    dir = 1
    for i in range(100):
        for j in range(n):
            turtle.setx(turtle.xcor() + 7 * dir)
            if k in l:
            # if isPrime(k):
                # print(k)
                numPrimes += 1
                turtle.pencolor("red")
            else:
                turtle.pencolor("black")
            turtle.dot(5)
            k += 1
        for j in range(n):
            turtle.sety(turtle.ycor() + 7 * dir)
            # if isPrime(k):
            if k in l:
                # print(k)
                numPrimes += 1
                turtle.pencolor("red")
            else:
                turtle.pencolor("black")
            turtle.dot(5)
            k += 1
        n += 1
        dir =- dir
    # print (k - 1, numPrimes)
    turtle.hideturtle()

plot(1)
