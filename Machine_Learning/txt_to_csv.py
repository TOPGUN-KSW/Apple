import pandas as pd
file = pd.read_csv(r'./Machine_Learning/Apple_attribute-6.txt')
new_csv_file = file.to_csv(r'./Machine_Learning/Apple_attribute-6.csv', index=None)