import pandas as pd

start = "2020-01-01"
end = "2020-11-25"

year_2020 = pd.date_range(start=start, end=end)
print(year_2020)
