import numpy as np
import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures 
from sklearn.metrics import r2_score

import matplotlib.pyplot as plt
import math

fib_data = pd.read_excel("FibPrimeGaps.xlsx", sheetname = "Gaps")

# Gaps


x = fib_data["x"][:-1].values.reshape(-1, 1)
y1 = fib_data["Fib Prime Differences"].values.reshape(-1, 1)
y2 = fib_data["log(differences)"].values.reshape(-1, 1)
y3 = fib_data["log(log(differences))"][1:].values.reshape(-1, 1)

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
plt.ylabel("Log(Nth gap)")
plt.legend(["Log(Nth Gap)", "Best Fit Line", "Best Fit Cubic Polynomial"])
plt.show()

reshaped_pred_lin = np.array(pred_lin).reshape(len(pred_lin),)
print reshaped_pred_lin

error = reshaped_pred_lin - y3.reshape(len(y3),)
print error
print max(error)
print min(error)
