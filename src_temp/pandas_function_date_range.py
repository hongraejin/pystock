import pandas as pd

result = pd.date_range('2020-01-01', end='2020-11-26')
print(result)

result = pd.date_range('2020-01-01', end='2020-11-26', freq='B')
print(result)
