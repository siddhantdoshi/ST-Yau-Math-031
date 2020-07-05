import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt
import math

import primefac

fib_data = pd.read_csv("FibPrime_2.csv")

# print fib_data

# print log_fib_prime_indices["x"].head()

# y = np.array(primefac.primes(1000000)).reshape(-1, 1)
# x = np.array(range(1, len(y) + 1)).reshape(-1, 1)

x = fib_data["x1"][:21].values.reshape(-1, 1)
y1 = fib_data["log(log(fib primes))"][:21].values.reshape(-1, 1)
# y2 = fib_data["ln of fibPrime Indices"].values.reshape(-1, 1)
# y3 = fib_data["log(fib prime indices)"].values.reshape(-1, 1)
# y4 = fib_data["fib_indices_rate_of_change"].values.reshape(-1, 1)
# y6 = fib_data["loga(log1a(loga(loga(index))))"][:8].values.reshape(-1, 1)
# y7 = fib_data["log(log(differences))"][2:21].values.reshape(-1, 1)
# y8 = fib_data["log(log(differences1))"][2:26].values.reshape(-1, 1)

print x
print y1

model_lin = LinearRegression()
best_fit_lin = model_lin.fit(x, y1)
pred_lin = model_lin.predict(x)
slope_lin = best_fit_lin.coef_
intercept_lin = best_fit_lin.intercept_

model_poly = LinearRegression(fit_intercept=False)
poly = PolynomialFeatures(degree = 3)
x_poly = poly.fit_transform(x)
best_fit_poly = model_poly.fit(x_poly, y1)
pred_poly = model_poly.predict(x_poly)
coefficients_poly = best_fit_poly.coef_

print "Slope:", slope_lin
print "Intercept:", intercept_lin
print "Poly coefficients:", coefficients_poly
print "r2 score line:", r2_score(y1, pred_lin)
print "r2 score poly:", r2_score(y1, pred_poly)

# print math.e ** pred_lin
# print
# print math.e ** pred_poly
# print pred_poly.reshape(1, -1)

plt.plot(x, y1, "ro", x, pred_lin, "b", x, pred_poly, "g")
plt.title("Regression Analysis")
plt.xlabel("N")
plt.ylabel("Log(Log(Nth Fibonacci Prime))")
plt.legend(["Log(Log(Nth Fibonacci Prime))", "Best Fit Line", "Best Fit Cubic Polynomial"])
plt.show()
