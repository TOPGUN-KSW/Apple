import pandas as pd
file = pd.read_csv(r'./Machine_Learning/Apple_sweetness6_c.txt')
new_csv_file = file.to_csv(r'./Machine_Learning/Apple_sweetness6_c.csv', index=None)