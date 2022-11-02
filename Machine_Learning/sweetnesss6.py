import pandas as pd
df1 = pd.read_csv('./Machine_Learning/apple_sweetness_c.csv')
text=open('./Machine_Learning/Apple_sweetness6_c.txt', 'w')
print("sweetness", file=text)
for i in range(0, 200):
  for j in range(1, 7):
    print(df1['Sweetness'][i], file=text)
text.close