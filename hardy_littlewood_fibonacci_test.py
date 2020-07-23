from hardy_littlewood_conjecture2_test import *
from fibonacci import fibonacci

# for i in range(5, 32):
# 	print i, check_conjecture2(fibonacci(i - 1), fibonacci(i - 2))

print check_conjecture2(fibonacci(1475), fibonacci(1474))
