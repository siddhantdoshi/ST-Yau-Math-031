import math
from prime_counting_function import prime_counter

def check_conjecture1(m, n):
	if prime_counter(m + n) <= prime_counter(m) + prime_counter(n):
		return True

	else:
		return False

def check_conjecture2(m, n):
	prime_counter = lambda x: x / math.log(x)

	if prime_counter(m + n) <= prime_counter(m) + prime_counter(n):
		return True

	else:
		return False
