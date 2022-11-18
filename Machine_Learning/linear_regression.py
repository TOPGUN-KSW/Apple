import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge


at = pd.read_csv('./Machine_Learning/Apple_attribute6.csv')
apple_attribute = at.to_numpy()
sw = pd.read_csv('./Machine_Learning/Apple_sweetness6.csv')
apple_sweetness = sw.to_numpy()
train_input = apple_attribute
train_target = apple_sweetness
train_input, test_input, train_target, test_target = train_test_split(apple_attribute, apple_sweetness, test_size=0.2)

poly = PolynomialFeatures(degree=3)
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)
test_scaled = ss.transform(test_poly)

ridge = Ridge(alpha = 10)
ridge.fit(train_scaled, train_target)
print(round(ridge.score(train_scaled, train_target), 4))
print(round(ridge.score(test_scaled, test_target), 4))
# print(test_scaled[1])
# print(ridge.predict(test_scaled))

import matplotlib.pyplot as plt #Ridge alpha값 찾기
train_score = [] 
test_score = []

alpha_list = [0.1, 1, 10, 30, 50, 70, 100]
for alpha in alpha_list:
  full_ridge = Ridge(alpha=alpha)
  full_ridge.fit(train_scaled, train_target)
  train_score.append(full_ridge.score(train_scaled, train_target))
  test_score.append(full_ridge.score(test_scaled, test_target))  
plt.plot(np.log10(alpha_list), train_score)
plt.plot(np.log10(alpha_list), test_score)
plt.xlabel('alpha')
plt.ylabel('R^2')
plt.show()

test = pd.read_csv('./Machine_Learning/test.csv')
test_input = test
poly.fit(test_input)
test_poly = poly.transform(test_input)
ss.fit(test_poly)
test_scaled = ss.transform(test_poly)

print(ridge.predict(test_scaled))

# from sklearn.linear_model import Lasso
# full_lasso = Lasso(alpha = 0.1)
# full_lasso.fit(train_scaled, train_target)
# print(round(full_lasso.score(train_scaled, train_target), 4))
# print(round(full_lasso.score(test_scaled, test_target), 4))

# import matplotlib.pyplot as plt #Lasso alpha값 찾기
# train_score = []
# test_score = []

# alpha_list = [0.001, 0.01, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.4, 0.5, 1, 10]
# for alpha in alpha_list:
#   full_lasso = Lasso(alpha=alpha)
#   full_lasso.fit(train_scaled, train_target)
#   train_score.append(full_lasso.score(train_scaled, train_target))
#   test_score.append(full_lasso.score(test_scaled, test_target))  
# plt.plot(np.log10(alpha_list), train_score)
# plt.plot(np.log10(alpha_list), test_score)
# plt.xlabel('alpha')
# plt.ylabel('R^2')
# plt.show()

'''
하이퍼파라미터 튜닝하는 방법
1. Gridsearch CV
params = {alpha:[100, 200, 300]}

2. Optuna 
'''