def fibonacci(n):
	fib0 = 0
	fib1 = 1
	fibn = 0

	if n == 0:
		return fib0

	if n == 1:
		return fib1

	for i in range(2, n + 1):
		fibn = fib0 + fib1
		fib0 = fib1
		fib1 = fibn

	return fibn

# print fibonacci(5)