import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

pageSpeeds = np.random.normal(3.0, 1.0, 1000)
purchaseAmount = 100 - (pageSpeeds + np.random.normal(0, 0.1, 1000)) * 3

# show as scatter plot
# plt.scatter(pageSpeeds, purchaseAmount)
# plt.show()

# do linear regression with scipy help
slope, intercept, r_value, p_value, stderr = stats.linregress(pageSpeeds, purchaseAmount)
# chech r-squared (once it near 1, its good)
rSquared = r_value ** 2
print('rSquared: ', rSquared)

# check predicted value
fitLine = slope * pageSpeeds + intercept
# redraw scatter with predicted value
plt.scatter(pageSpeeds, purchaseAmount)
plt.plot(pageSpeeds, fitLine, c='y')
plt.show()