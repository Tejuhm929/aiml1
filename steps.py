import pandas as pd
import numpy as np
data={'day':[1,2,3,4,5,6,7,8,9,10],
      'steps':[4335,9552,7332,4504,5335,7552,6332,6504,8965,7689]}
p=pd.DataFrame(data)
p['steps']=p['steps']+1000
print(p['steps'])
a=p['steps']>=7000
print(a)
print(p.loc[p['steps']<7000])
print(p['steps'].min)
