import primefac
import sympy

degree = 2

def num_primes(start, stop, coef):
	num_primes = 0

	for i in xrange(start, stop + 1):
		if primefac.isprime(coef[0] * i ** 2 + coef[1] * i + coef[2]):
			num_primes += 1

	return num_primes

prime_poly_list = [(num_primes(0, 1000, [c1, c2, c3]), [c1, c2, c3]) for c1 in xrange(1, 22) for c2 in xrange(1, 22) for c3 in xrange(1, 22)]
a = max(prime_poly_list)
best_coef = a[1]
most_primes = a[0]

print best_coef, most_primes

# print num_primes(0, 1000, [7, 7, 17])
