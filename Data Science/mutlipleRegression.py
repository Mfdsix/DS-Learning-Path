import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler

# load data from excel
dataFrame = pd.read_excel("source/cars.xls")
#print(dataFrame.head())

# specified what data to get
datas = dataFrame[['Mileage', 'Price']]

# data grouping
bins = np.arange(0, 50000, 10000) # 0, 10000, 20000, 30000, 40000, 50000
groups = datas.groupby(pd.cut(datas['Mileage'], bins))
mean = groups.mean()
# groups['Price'].plot.line()
# plt.show()

# scaling data
scale = StandardScaler()
x = dataFrame[['Mileage', 'Cylinder', 'Doors']]
y = dataFrame['Price']

x = scale.fit_transform(x.values)
x = sm.add_constant(x)

est = sm.OLS(y, x).fit()
# print(est.summary())

# check door prices
doorPrices = y.groupby(dataFrame.Doors).mean()
# print(doorPrices)

# scaling your multiple feature variables into the same scale used to train the model
scaled = scale.transform([[45000, 8, 4]])
scaled = np.insert(scaled[0], 0, 1)
predicted = est.predict(scaled)

print('Scaled: ', scaled)
print('Predicted:', predicted)
