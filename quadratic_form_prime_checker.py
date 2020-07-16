
import sympy
#ax^2 + bx + c
print("x^2 + x +  c : number of primes")
#range can be adjusted
under50 = []
from50to100 = []
from100to150 = []
above150 = []
for c in range(-1001,1002,2):
        if c == 0:
                continue
        primesIn = []
        for x in range(-1000,1001):
                j =  pow(x,2) + x + c
                if sympy.isprime(j):
                        primesIn.append(j)
        #print(primesIn)
        if len(primesIn) < 50:
              under50.append(c)
        elif len(primesIn) >= 50 and len(primesIn) < 100:
                from50to100.append(c)
        elif len(primesIn) >= 100 and len(primesIn) < 150:
                from100to150.append(c)
        else:
                above150.append(c)


print("Under 50:", len(under50))
print("______________________________________________________________")
print("50 to 99:", len(from50to100))
print("______________________________________________________________")
print("100 to 149:", len(from100to150))
print("______________________________________________________________")
print("150 and above:", len(above150))
print("______________________________________________________________")

#________________________________________________________________________
"""import sympy
primesIn = []
c = 41
for x in range(-100,101):
        j =  pow(x,2) + x + c
        if sympy.isprime(j):
                primesIn.append(j)
print(primesIn)

if c > 0:
        print("x^2 + x + ", c, ":", len(primesIn))
elif c < 0:
        print("x^2 + x - ", -c, ":", len(primesIn))"""

