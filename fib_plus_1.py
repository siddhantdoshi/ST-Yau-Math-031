import primefac
from fibonacci import fibonacci
import math

num_primes = 0

for i in range(1, 10000):
	if primefac.isprime(int(round(math.log(fibonacci(i))))):
		num_primes += 1

print num_primes
