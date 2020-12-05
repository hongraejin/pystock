import pandas._testing as tm
import numpy as np
import pandas as pd

def unpivot(frame):
    N, K = frame.shape
    data = {
        'value': frame.to_numpy().ravel("F"),
        'variable':np.asarray(frame.columns).repeat(N),
        'date': np.tile(np.asarray(frame.index), K)
    }
    return pd.DataFrame(data, columns =['date','variable','value'])

df = unpivot(tm.makeTimeDataFrame(3))
print(df)