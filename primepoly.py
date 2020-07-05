from math import sqrt; from itertools import count, islice
import itertools
from itertools import product


#is n prime?
def isPrime(n):
    #https://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
    return n > 1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

#find P(x) using the polyList to represent the polynomial
def findSingleValue(polyList, x):

    #https://stackoverflow.com/questions/18093509/how-can-i-create-functions-that-handle-polynomials
    return sum((a*x**i for i,a in enumerate(polyList)))



#is the polynomial prime for x <= p - 1?
def isPolyPrime(polyList, prime):
    #polyValue = 0
    for x in range(prime - 1):
        polyValue = sum((a*x**i for i,a in enumerate(polyList)))
        if not isPrime(polyValue):
            return False

    return True

#generate the next combo, given the previous combo
def genCombo(combo, LB, HB):
    deg = len(combo)
    combo = list(combo)
    index = deg - 1
    while index >= 0:
        if combo[index] < HB:
            combo[index] += 1
            index = -1
        elif combo[index] == HB:
            combo[index] = LB
        index -= 1
    combo = tuple(combo)
    return combo



#main function
def verifyPrime():

    prime = int(input("Enter the prime number you want to find a poly for: "))
    LB = int(input("Enter the lower bound: "))
    HB = int(input("Enter the higher bound: "))
    deg = int(input("Enter the degree of the polynomial: "))
    lowDegPoly= input("Press n if you do not want to include lower degree polynomials: ")

    allCombosNum = (abs(HB - LB))**deg - 1



    #creates list of all possible tuples that represent a poly


    print("possible combos (including constant func): ")
    print(allCombosNum)

    goodPolyList = []
    combo = ()

    #create the first combo - this is used as the basis to generate more combos
    for x in range(deg):
        combo += (LB,)



    for x in range(allCombosNum):
        polyList = []
        polyList.append(prime)
        for coef in combo:
            polyList.append(coef)
        #now has a list of the prime and coefs; p + a1*x + a2*x^2 + ...
        isGoodPoly = isPolyPrime(polyList, prime)
        if isGoodPoly and not(lowDegPoly == "n" and combo[deg - 1] == 0):
            goodPolyList.append(polyList)


        #personal usage: keeps track of how many more combos it needs to go through
        numLeft = allCombosNum - x
        if (numLeft % 100000) == 0:
            print(numLeft)


        #create the next combo
        combo = genCombo(combo, LB, HB)


    print("################################################")
    print("poly generating finished")
    print()
    print(goodPolyList)

    #bonus stuff

    #goes over items in the goodPolyList and shows what primes each generates

    for item in goodPolyList:

        primeList = []
        for x in range(prime - 1):
            primeList.append(findSingleValue(item, x))
        print()
        print("List of primes that" , item, "generates: ")
        print(primeList)

    print()

    print("There are" , len(goodPolyList) , "good polynomials for", prime ,
         "with bounds" , LB , " to" , HB, "inclusive up to degree" , deg)

    verifyPrime()

verifyPrime()
