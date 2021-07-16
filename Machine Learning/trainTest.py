import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

# find best rsquare from setting polynomial value
# its weird man xixixi, when your polynomial value higher, your rSquare score being higher :)
maxP = 15
r2Scores = []

# initial data
np.random.seed(2)
x = np.random.normal(3.0, 1.0, 100)
y = np.random.normal(50.0, 30.0, 100) / x

# define train and test splitting
trainX = x[:80]
trainY = y[:80]
testX = x[80:]
testY = y[80:]

# use polynomial regression
def findRegression(x, y, p) :
    poly = np.poly1d(np.polyfit(x, y ,p))
    # linspace = np.linspace(0, 5.5, 100)
    # plt.scatter(x, y)
    # plt.plot(linspace, poly(linspace), c='r')
    # plt.show()
    return poly

for i in range(maxP):
    polynominal = findRegression(trainX, trainY, i)
    # test data
    # findRegression(testX, testY, 8)

    # calculate rSquare
    rSquare = r2_score(trainY, polynominal(trainX))
    print(i ,' => rsquare: ', rSquare)
    r2Scores.append(rSquare)

print(r2Scores)