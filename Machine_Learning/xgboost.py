import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler
from xgboost import XGBRegressor


at = pd.read_csv('./Machine_Learning/Apple_attribute.csv')
apple_attribute = at.to_numpy()
sw = pd.read_csv('./Machine_Learning/Apple_sweetness.csv')
apple_sweetness = sw.to_numpy()
train_input, test_input, Y_train, Y_test = train_test_split(apple_attribute, apple_sweetness, test_size=0.2)

poly = PolynomialFeatures(degree=3)
poly.fit(train_input)
train_poly = poly.transform(train_input)
test_poly = poly.transform(test_input)

ss = StandardScaler()
ss.fit(train_poly)
X_train = ss.transform(train_poly)
X_test = ss.transform(test_poly)

# 1. 모델 선언
xgb  = XGBRegressor()

# 2. 모델 훈련 fit()함수
xgb.fit(X_train, Y_train)

# 3. 모델 예측 predict()함수
Y_pred = xgb.predict(X_test)

# 4. score()
xgb.score(X_train, Y_train)