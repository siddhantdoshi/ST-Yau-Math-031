import sympy

def prime_counter(n):
	count = 0

	for i in range(1, n + 1):
		if sympy.isprime(i):
			count += 1

	return count
