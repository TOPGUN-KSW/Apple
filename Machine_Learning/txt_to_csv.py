import pandas as pd
file = pd.read_csv(r'./Machine_Learning/Apple_attribute.txt')
new_csv_file = file.to_csv(r'./Machine_Learning/Apple_attribute.csv', index=None)