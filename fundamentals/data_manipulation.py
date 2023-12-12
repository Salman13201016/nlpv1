import numpy as np

data = {"name":['x','y','z','a','b','c'],
        'age': [18,20,18,np.nan,np.nan,21],
        'salary': ['20','25',np.nan,np.nan,'50','60'],
        'dept':['IT','Accounts','CSIT',np.nan,np.nan,'finance']
}

import pandas as pd

df = pd.DataFrame(data)
data_after_filter = df[(df['age']<20) & (df['salary']=='40')]

print(df)


# data_str_contains = df[df['dept'].str.contains('IT')]



drop_df = df.dropna(thresh=3)

drop_replace_with_default_value = df.replace(np.nan,'0')



df_forward = df.fillna(method='ffill')
df_backward = df.fillna(method='bfill')
# print("forward",df_forward)
# print("backward",df_backward)

df_interpolate = df.interpolate()
print("interpolate",df_interpolate)
