z = int(input("How many numbers:"))
n = 3

for y in range(1, z + 1):
	primeFactors = []
	primeFlag = True
	l = pow(y,n) - pow(y-1,n)
	for i in range(2,l):
		if l % i == 0:
			primeFactors.append(i)
			primeFlag = False
	if primeFlag is False:
		print(y,l,"not prime",primeFactors)
	else:
		print(y,l,"prime")
