import joblib
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import StandardScaler

model = joblib.load('./Machine_Learning/model.pkl')

test = pd.read_csv('./Machine_Learning/test.csv')
test_input = test
poly = PolynomialFeatures(degree=3)
poly.fit(test_input)
test_poly = poly.transform(test_input)
ss = StandardScaler()
ss.fit(test_poly)
test_scaled = ss.transform(test_poly)


text=open('./Machine_Learning/sugarlevel.txt', 'w')
for i in model.predict(test_scaled):
    if i == model.predict(test_scaled)[len(model.predict(test_scaled))-1]:
        print(i[0], file=text)
    else:
        print(i[0], file=text, end =', ')
text.close()