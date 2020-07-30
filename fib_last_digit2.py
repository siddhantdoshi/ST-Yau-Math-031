nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0
fibs = []
# check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < nterms:
       fibs.append(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
digit = []

for x in fibs:
    digit.append(x%10)
print(digit)
digitCount = [0,0,0,0,0,0,0,0,0,0]
for x in digit:
    if x == 1:
        digitCount[x] += 1
    elif x == 2:
        digitCount[x] += 1
    elif x == 3:
        digitCount[x] += 1
    elif x == 4:
        digitCount[x] += 1
    elif x == 5:
        digitCount[x] += 1
    elif x == 6:
        digitCount[x] += 1
    elif x == 7:
        digitCount[x] += 1
    elif x == 8:
        digitCount[x] += 1
    elif x == 9:
       digitCount[x] += 1
    elif x == 0:
        digitCount[x] += 1
print(digitCount)