from prime_counting_function import prime_counter
from fibonacci import fibonacci

def primes_between_fibonacci(n):
	return prime_counter(fibonacci(n + 1)) - prime_counter(fibonacci(n))

for i in range(35):
	print i, fibonacci(i), primes_between_fibonacci(i)
