import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# generate some datas
np.random.seed(2)
pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = np.random.normal(50.0, 10.0, 1000) / pageSpeeds

# show as scatter plot
# plt.scatter(pageSpeeds, purchaseAmount)
# plt.show()

# set polynomial degree
polyfit = np.polyfit(pageSpeeds, purchaseAmount, 4)
polynomial = np.poly1d(polyfit)

# draw on scatter plot with predicted value
linspace = np.linspace(0, 7, 1000)
plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(linspace, polynomial(linspace), c="r")
plt.show()

# get rSquare value
rSquare = r2_score(purchaseAmount, polynomial(pageSpeeds))
print('rSquare: ', rSquare)