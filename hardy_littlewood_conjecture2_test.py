from prime_counting_function import prime_counter

def check_conjecture(m, n):
	if prime_counter(m + n) <= prime_counter(m) + prime_counter(n):
		return True

	else:
		return False
