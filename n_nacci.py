def n_nacci(order, terms):
	n_nacci_series = [0] * (order - 1) + [1] # Creates a list with (n - 1) zeroes and then a 1

	for i in range(terms - order):
		n_nacci_series.append(sum(n_nacci_series[i : i + order])) # Each element is the sum of the previous n elements

	return n_nacci_series

print("This program will output any number of terms of an n-nacci sequence.\n")

n = int(input("Enter the order ('n') of the series: "))
desired_terms = int(input("Number of terms to be displayed: "))

print("\n" + str(n_nacci(n, desired_terms)))
