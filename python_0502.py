from selectorlib import Extractor
import requests

# Create an Extractor by reading from the YAML file
e = Extractor.from_yaml_file('search_results.yml')

# Download the page using requests
r = requests.get('https://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=headphones')
# Pass the HTML of the page and create
data = e.extract(r.text)
# Print the data
print(data)

