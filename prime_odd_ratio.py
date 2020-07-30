import primefac

num_odd = 10000000
num_primes = 0

for i in xrange(1, num_odd, 2):
	if primefac.isprime(i):
		num_primes += 1

print (2.0 * num_primes) / num_odd
