import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge
import joblib

at = pd.read_csv('./Machine_Learning/Apple_attribute6.csv')
apple_attribute = at.to_numpy()
sw = pd.read_csv('./Machine_Learning/Apple_sweetness6.csv')
apple_sweetness = sw.to_numpy()
train_input = apple_attribute
train_target = apple_sweetness

poly = PolynomialFeatures(degree=3)
poly.fit(train_input)
train_poly = poly.transform(train_input)

ss = StandardScaler()
ss.fit(train_poly)
train_scaled = ss.transform(train_poly)

ridge = Ridge(alpha = 10)
ridge.fit(train_scaled, train_target)
print(round(ridge.score(train_scaled, train_target), 4))

joblib.dump(ridge, './Machine_Learning/model.pkl')

model = joblib.load('./Machine_Learning/model.pkl')

test = pd.read_csv('./Machine_Learning/test.csv')
test_input = test
poly.fit(test_input)
test_poly = poly.transform(test_input)
ss.fit(test_poly)
test_scaled = ss.transform(test_poly)

print(model.predict(test_scaled))