import primefac

is_prime = []

for i in xrange(1, 1000001):
	last_digit = i % 10

	if last_digit in [4, 6, 8]:
		is_prime.append((i, 3 * last_digit - 1, primefac.isprime(3 * last_digit - 1)))

	elif last_digit in [1, 3, 7, 9]:
		is_prime.append((i, 3 * last_digit - 10, primefac.isprime(3 * last_digit - 10)))

	elif last_digit == 2:
		is_prime.append((i, 3 * last_digit + 1, primefac.isprime(3 * last_digit + 1)))

	elif last_digit == 5:
		is_prime.append((i, 3 * last_digit + 2, primefac.isprime(3 * last_digit + 2)))
		is_prime.append((i, 3 * last_digit - 2, primefac.isprime(3 * last_digit - 2)))

	elif last_digit == 0:
		is_prime.append((i, 3 * last_digit + 1, primefac.isprime(3 * last_digit + 1)))
		is_prime.append((i, 3 * last_digit - 1, primefac.isprime(3 * last_digit - 1)))

	else:
		pass

print all(map(lambda x: x[2], is_prime))
print len(filter(lambda x: x[2] == True, is_prime))
print len(filter(lambda x: x[2] == False, is_prime))
