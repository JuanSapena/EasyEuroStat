
from easy_eurostat import get_eurostat_dataset

dataset = "teilm020"
url = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/" + dataset + "/?format=TSV&compressed=true"
print(url)


df = get_eurostat_dataset("teilm020")
print(df)