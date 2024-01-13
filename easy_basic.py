import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import os
dirname = os.path.dirname(__file__)

from easy_eurostat import file_age
from easy_eurostat import download_url
from easy_eurostat import get_eurostat_dictionary
from easy_eurostat import get_eurostat_dataset
from easy_eurostat import get_eurostat_geodata

dataset = "teilm020"
url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/" + dataset + "/?format=TSV&compressed=true"
print(url)


df = get_eurostat_dataset("teilm020")
print(df)

df = get_eurostat_dataset("teilm020", replace_codes=True, transpose=False, keep_codes=['geo', 's_adj'])
df = df[(df['age'] == 'Total') & (df['sex'] == 'Total')]
print(df)

countries = get_eurostat_geodata(lvl=0)

print(countries.columns)

df.columns

df = pd.merge(countries, df, right_on='geo', left_on='NUTS_ID')
ax = df.plot(column='2023-09', figsize=(10,10), legend=True)
ax.set_xlim(2000000, 7000000)
ax.set_ylim(1000000, 6000000)
ax.set_title('Unemployment in the European Union')
plt.show()