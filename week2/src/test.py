import os
import requests
#from lxml import html
from lxml import etree
import matplotlib.pyplot as plt

# Constants for the URL and XPath

url = 'https://www.worldometers.info/world-population/china-hong-kong-sar-population/'

res = requests.get(url=url)
html = etree.HTML(res.text)
lis = html.xpath('/html/body/div[2]/div[3]/div/div/div[5]/table/tbody/tr')
print(res.status_code)
print(len(lis))
"""
URL = 'https://www.census2021.gov.hk/en/district_profiles.html'
DATA_XPATH = '//path_to_data_in_the_html_document'  # Update with actual path


# Fetch the data
def fetch_page(url):
    response = requests.get(url)
    return response.content


def parse_page(content):
    tree = html.fromstring(content)
    data = tree.xpath(DATA_XPATH)
    # Extract the necessary data fields
    return data


def visualize_data(data):
    # Example visualization with mock data structure
    districts = [entry['district'] for entry in data]
    populations = [entry['population'] for entry in data]

    plt.figure(figsize=(10, 8))
    plt.bar(districts, populations)
    plt.xlabel('Districts')
    plt.ylabel('Population')
    plt.title('Population Distribution Across Districts')
    plt.show()


if __name__ == '__main__':
    page_content = fetch_page(URL)
    census_data = parse_page(page_content)
    visualize_data(census_data)
"""