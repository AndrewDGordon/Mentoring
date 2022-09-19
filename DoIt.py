# on wsl
# sudo apt install python3-pandas

import pandas as pd
import numpy as np

from csrankings import *
#print(areadict)
#print(confdict)

groups = pd.read_csv("groups.csv")
print(groups)

country_info = pd.read_csv("country-info.csv")
cs_rankings = pd.read_csv("csrankings.csv")
cs_rankings.rename(columns = {'affiliation':'institution'}, inplace=True)

generated_author_info = pd.read_csv("generated-author-info.csv")
generated_author_info.rename(columns = {'dept':'institution'}, inplace=True)

#print(country_info)
print(cs_rankings)
#print(generated_author_info)

df1 = country_info[ country_info.countryabbrv=="uk" ]
#print(df1.shape) # 43 institutions in UK

df2 = pd.merge(generated_author_info, df1)
df3 = pd.merge(df2,groups)
df4 = pd.merge(df3,cs_rankings)

# https://pbpython.com/pandas-pivot-table-explained.html
df = pd.pivot_table(df4, values='count', index=['name','institution','homepage'], columns=['group'], aggfunc=np.sum, fill_value=0)

print(df.shape)
df.to_csv('output.csv') 
print(df)
