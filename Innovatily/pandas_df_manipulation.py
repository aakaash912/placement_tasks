import pandas as pd
data = {
'Product': ['A', 'B', 'A', 'C', 'B', 'C'],
'Sales': [100, 200, 150, 300, 250, 400],
'Region': ['North', 'South', 'North', 'East', 'South', 'East']
}
df = pd.DataFrame(data)

df.groupby('Product').sum()
print(df)

df.groupby('Region').max()
print(df)

df['discounted_price']=df['Sales']*0.9
print(df)
