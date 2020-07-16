from prime_counting_function import prime_counter

def check_conjecture(m, n):
	if prime_counter(m + n) <= prime_counter(m) + prime_counter(n):
		return True

	else:
		return False

all_true = []

for i in range(2, 101):
	for j in range(2, 101):
		all_true.append(check_conjecture(i, j))

print all(all_true)
