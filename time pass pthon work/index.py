import pandas as pd 
import numpy as np 
s1 = pd.Series(data=[10,32,44,32,54,65,65],index= range(100,107))
print("index  data")
print(s1)
print(type(s1))
di = {"name":["aditya","aman","azeem"],"age":[23,22,43]}
df = pd.DataFrame(di)
print(df)
