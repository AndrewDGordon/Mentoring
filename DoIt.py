# on wsl
# sudo apt install python3-pandas

import json
import io
import pandas as pd

from csrankings import *
print(areadict)
print(confdict)

country_info = pd.read_csv("country-info.csv")
cs_rankings = pd.read_csv("csrankings.csv")
cs_rankings.rename(columns = {'affiliation':'institution'}, inplace=True)

generated_author_info = pd.read_csv("generated-author-info.csv")
generated_author_info.rename(columns = {'dept':'institution'}, inplace=True)


#print(country_info)
#print(cs_rankings)
#print(generated_author_info)

df1 = country_info[ country_info.countryabbrv=="uk" ]
print(df1.shape) # 43 institutions in UK

df2 = pd.merge(generated_author_info, df1)
df3 = df2['area'].map(confdict)

print(df3.shape)
df3.to_csv('output.csv') 
