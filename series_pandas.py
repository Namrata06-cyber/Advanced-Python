import pandas as pd
#create a series from a list
ser=pd.Series([10,20,30,40,50])
print(ser)
#create a series with a custom index
ser=pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(ser)