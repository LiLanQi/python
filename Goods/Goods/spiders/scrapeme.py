import scrapy
import os
import selectorlib

class GoodsSpider(scrapy.Spider):
    name = 'goods'

    # Create Extractor for listing page
    listing_page_extractor = selectorlib.Extractor.from_yaml_file(
        os.path.join(os.path.dirname(__file__), '../selectorlib_yaml/dropShippingListingPage.yml'))
    # Create Extractor for product page
    product_page_extractor = selectorlib.Extractor.from_yaml_file(
        os.path.join(os.path.dirname(__file__), '../selectorlib_yaml/dropShippingProductPage.yml'))

    def start_requests(self):
        urls = [
            'https://dropshipping-products.automizely.com/products?p='
        ]
        for url in urls:
            yield scrapy.Request(url=url, meta={'index': 1})


    def parse(self, response):
        # Extract data using Extractor
        index = response.meta['index']
        index = index + 1
        data = self.listing_page_extractor.extract(response.text)
        data['next_page'] = 'https://dropshipping-products.automizely.com/products?p={0}'.format(index)

        if 'next_page' in data:
            yield scrapy.Request(data['next_page'], callback=self.parse, meta={"index": index})
        for p in data['product_page']:
            p = "https://dropshipping-products.automizely.com" + p
            yield scrapy.Request(p, callback=self.parse_product)



    def parse_product(self, response):
        # Extract data using Extractor
        # print(response.text)
        with open("123.txt",'w', encoding='utf-8') as file:
            file.write(response.text)



if __name__ == '__main__':
    from scrapy import cmdline
    args = "scrapy crawl goods".split()
    cmdline.execute(args)