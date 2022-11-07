import pandas as pd
file = pd.read_csv(r'./Machine_Learning/Apple_sweetness-3.txt')
new_csv_file = file.to_csv(r'./Machine_Learning/Apple_sweetness6-3.csv', index=None)