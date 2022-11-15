import pandas as pd
file = pd.read_csv(r'./Machine_Learning/Apple_attribute6.txt')
new_csv_file = file.to_csv(r'./Machine_Learning/Apple_attribute6.csv', index=None)