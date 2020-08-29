import numpy as np
import pandas as pd
from decimal import *

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt
import math

fib_data = pd.read_csv("FibonacciPrimes.csv")
fib_gaps_data = pd.read_csv("FibPrimeGaps.csv")

lucas_data = pd.read_csv("LucasPrimes.csv")
lucas_gaps_data = pd.read_csv("LucasPrimeGaps.csv")
lucas_gaps_indices_data = pd.read_csv("LucasPrimeIndicesGaps.csv")

"""
y = fib_data["FibPrimes"]
gaps = []

for fib1, fib2 in zip(y[y.index > 0], y[y.index < y.size - 1]):
	gaps.append(int(fib1) - int(fib2))

pd_gaps = pd.Series(map(str, gaps))

print len(pd_gaps)

pd_log_gaps = map(str, np.log10(map(Decimal, gaps)))

print len(pd_log_gaps)

pd_log_log_gaps = map(str, np.log10(np.log10(map(Decimal, gaps[1:]))))
pd_log_log_gaps = np.insert(pd_log_log_gaps, 0, "0")

print len(pd_log_log_gaps)

# print np.array([np.arange(1, 31), pd_gaps, pd_log_gaps, pd_log_log_gaps])

fib_gaps = pd.DataFrame(np.array([np.arange(1, 31), pd_gaps, pd_log_gaps, pd_log_log_gaps]).transpose(), columns = ["x", "Fib Prime Differences", "log(differences)", "log(log(differences))"])

print fib_gaps

fib_gaps.to_csv("FibPrimeGaps.csv")
"""

# Gaps

"""
x = fib_gaps_data["x"][:-1].values.reshape(-1, 1)
y1 = fib_gaps_data["Fib Prime Differences"].values.reshape(-1, 1)
y2 = fib_gaps_data["log(differences)"].values.reshape(-1, 1)
y3 = fib_gaps_data["log(log(differences))"][1:].values.reshape(-1, 1)
"""
"""
x = lucas_gaps_data["x"].values.reshape(-1, 1)
y1 = lucas_gaps_data["Lucas Primes"].values.reshape(-1, 1)
y2 = lucas_gaps_data["log(differences)"]
y3 = pd.Series(np.log(i) if i > 0 else 0 for i in y2)
y2 = y2.values.reshape(-1, 1)

lucas_gaps_data["log(log(differences))"] = y3
lucas_gaps_data.to_csv("LucasPrimeGaps.csv")
"""

# Indices of Gaps
"""
x = fib_data["x"][:-1].values.reshape(-1, 1)
y1 = fib_data["Fib Prime Indices"].values.reshape(-1, 1)
y2 = fib_data["Gaps"][:-1].values.reshape(-1, 1)
y3 = fib_data["ln(gaps)"][:-1].values.reshape(-1, 1)
"""
# print x
# print y1
# print y2
# print y3

model_lin = LinearRegression()
best_fit_lin = model_lin.fit(x, y3)
pred_lin = model_lin.predict(x)
slope_lin = best_fit_lin.coef_
intercept_lin = best_fit_lin.intercept_

model_poly = LinearRegression(fit_intercept=False)
poly = PolynomialFeatures(degree = 3)
x_poly = poly.fit_transform(x)
best_fit_poly = model_poly.fit(x_poly, y3)
pred_poly = model_poly.predict(x_poly)
coefficients_poly = best_fit_poly.coef_

print "Slope:", slope_lin
print "Intercept:", intercept_lin
print "Poly coefficients:", coefficients_poly
print "r2 score line:", r2_score(y3, pred_lin)
print "r2 score poly:", r2_score(y3, pred_poly)

plt.plot(x, y3, "ro", x, pred_lin, "b", x, pred_poly, "g")
plt.title("Regression Analysis")
plt.xlabel("N")
plt.ylabel("Log(Log(Nth gap))")
plt.legend(["Log(Log(Nth Gap))", "Best Fit Line", "Best Fit Cubic Polynomial"])
plt.show()

reshaped_pred_lin = np.array(pred_lin).values.reshape(len(pred_lin),)
print reshaped_pred_lin

error = reshaped_pred_lin - y3.values.reshape(len(y3),)
print error
print max(error)
print min(error)
