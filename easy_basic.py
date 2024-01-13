import os

from easy_eurostat import get_eurostat_dataset

dirname = os.path.dirname(__file__)
#cache = dirname + "\cache"

dataset = "teilm020"
url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/" + dataset + "/?format=TSV&compressed=true"
print(url)


df = get_eurostat_dataset("teilm020")
print(df)