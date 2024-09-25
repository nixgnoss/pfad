import os
import requests
from lxml import etree
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import pandas as pd

# Load environment variables
load_dotenv()
df=pd.DataFrame(columns=["YEAR","POPULATION"])

# Constants

url = 'https://www.worldometers.info/world-population/china-hong-kong-sar-population/'

res = requests.get(url=url)
html = etree.HTML(res.text)
lis = html.xpath('/html/body/div[2]/div[3]/div/div/div[5]/table/tbody/tr')
print(res.status_code)
print(len(lis))

for li in lis:
    year = (li.xpath('./td[1]/text()'))
    population = (li.xpath('./td[2]/strong/text()'))
    print(year, population)
    df.loc[len(df.index)] = [year, population]

df.to_excel("Population.xlsx",sheet_name="Population",na_rep="")

df = pd.read_excel("Population.xlsx",sheet_name="Population")
x = df['YEAR']
y = df['POPULATION']

plt.figure(figsize=(10, 6))
plt.plot(x,y)
plt.title('Hong Kong SAR Population Over Time')
plt.xlabel('Year')
plt.ylabel('Population')
plt.grid(True)
plt.show()

